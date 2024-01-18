import numpy as np
import time
import matplotlib.pyplot as plt
import random

def to_arr_pad(s1, s2):
    if len(s1) < len(s2):
        diff = len(s2) - len(s1)
        zeros = "0" * diff
        s1 = zeros + s1
    else:
        diff = len(s1) - len(s2)
        zeros = "0" * diff
        s2 = zeros + s2
    s1 = [int(x) for x in list(s1)][::-1]
    s2 = [int(x) for x in list(s2)][::-1]
    s1.append(0)
    s1.append(0)
    s2.append(0)
    s2.append(0)
    return s1, s2

def update_ans(i, ans):
    # print(i, ans)
    quotient = int(ans[i]/2)
    remainder = ans[i] % 2
    ans[i] = remainder
    if i == 1 or i == 2:
        ans[3] += quotient
    else:
        ans[i+1] += quotient
        ans[i-2] += quotient
    # print(ans)
    return ans
    

def add(s1, s2):
    s1, s2 = to_arr_pad(s1, s2)
    # print(s1, s2)
    ans = [0] * len(s1)
    unsolved = True
    count = 0
    for i in range(len(s1)):
        ans[i] += s1[i] + s2[i]
    while unsolved:
        # loops through the lists backwards
        count += 1
        for i in range(len(s1)):
            if ans[i] > 1:
                quotient = int(ans[i]/2)
                remainder = ans[i] % 2
                ans[i] = remainder
                if i == 1 or i == 2:
                    ans[3] += quotient
                else:
                    ans[i+1] += quotient
                    ans[i-2] += quotient
                # ans = update_ans(i, ans)
        # print(ans)
        if any(val not in (0, 1) for val in ans):
            unsolved = True
        else:
            unsolved = False
    return ans[::-1], count

def randomFib(length):
    return ''.join(random.choice('01') for _ in range(length))



if __name__ == "__main__":
    # print(add("1110", "1110"))
    s1 = "111100"
    s2 = "10011010"
    # print(add(s1, s2))
    x = np.arange(1, 2000, 1)
    y = []
    for i in x:
        print(i)
        a = randomFib(i)
        b = randomFib(i)
        # print(a, b)
        # start = time.time()
        ans, count = add(a, b)
        y.append(count)
        # y.append(time.time() - start)
    plt.plot(x[1:], y[1:])
    plt.show()
    print("Done")
    


"""
notes:
- need to prove that the sum of any two numbers in base fibonacci won't overflow more than two spaces"""