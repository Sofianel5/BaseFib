import time
import matplotlib.pyplot as plt
import numpy as np
import random
from tqdm import tqdm
from utils import filterOutliers, smooth

TABLE_LOOKUP = False
FIBS = [0, 1]

def deconstructN(fibs, n):
     left = n
     idxs = []
     while left > 0:
            if fibs[-1] <= left:
                idxs.append(len(fibs) - 1)
                left -= fibs[-1]
            fibs.pop()
     return idxs

def constructFib(idxs):
     s = ""
     end = idxs[0]+1
     for i in range(end):
        if idxs[-1] == i:
            s += "1"
            idxs.pop()
        else:
            s += "0"
     return s[::-1]

def computeFibs(n):
    fibs = [0, 1]
    while fibs[-1] < n:
        fibs.append(fibs[-1] + fibs[-2])
    return fibs

def computeFibsMemo(n):
    global FIBS
    while FIBS[-1] < n:
        FIBS.append(FIBS[-1] + FIBS[-2])
    return FIBS

def dec2fib(n):
     fibs = computeFibsMemo(n) if TABLE_LOOKUP else computeFibs(n)
     idxs = deconstructN(fibs.copy(), n)
     if idxs:
        return constructFib(idxs)
     return "0"

def fib2dec(fibnum):
     if len(fibnum) <= 1:
        return 0
     l = [(fibnum[-1] == '1', 0), (fibnum[-2] == '1', 1)]
     for i, c in enumerate(fibnum[::-1]):
        if i > 1:
            l.append((c == '1', l[i-1][1] + l[i-2][1]))
     return sum([pos*val for pos,val in l])

def addFibs(fib1, fib2):
     return dec2fib(fib2dec(fib1) + fib2dec(fib2))

def multFibs(fib1, fib2):
    return dec2fib(fib2dec(fib1) * fib2dec(fib2))

def randomFib(len):
    return "".join([str(random.randint(0, 1)) for _ in range(len)])

def toCanonicalForm(fib):
    return dec2fib(fib2dec(fib))

def add(fib1, fib2):
    fib1, fib2 = toCanonicalForm(fib1), toCanonicalForm(fib2)
    if len(fib1) < len(fib2):
        fib1, fib2 = fib2, fib1

    fib2 = "0"*(len(fib1) - len(fib2)) + fib2

    res, carry = ["0"]*len(fib1), ["0"]*len(fib1)

    for i in range(len(fib1)):
        if fib1[i] == "0" and fib2[i] == "0":
            continue
        elif (fib1[i] == "1" and fib2[i] == "0") or (fib1[i] == "0" and fib2[i] == "1"):
            if res[i] == "0":
                res[i] = "1"
            else:
                res[i]


if __name__ == "__main__":
    # Test conversion
    for i in range(10000):
        if fib2dec(dec2fib(i)) != i:
            print("ERROR: {} != {}".format(fib2dec(dec2fib(i)), i))

    # Test addition
    for i in range(100):
        for j in range(100):
            if addFibs(dec2fib(i), dec2fib(j)) != dec2fib(i+j):
                print("ERROR: {} + {} != {}".format(dec2fib(i), dec2fib(j), dec2fib(i+j)))

    # Graph addition time as function of number of digits
    LEN_MAX_TEST = 20000
    x = np.arange(1, LEN_MAX_TEST, 1)
    y = []
    for i in tqdm(x):
        a = randomFib(i)
        b = randomFib(i)
        start = time.time()
        addFibs(a, b)
        y.append(time.time() - start)
    x, y = filterOutliers(x, y)
    plt.plot(x[1:], y[1:])
    plt.show()
    print("Done")
