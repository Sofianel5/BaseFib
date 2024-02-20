from fibs import randomFib, fib2dec, computeFibs
import numpy as np
from tqdm import tqdm
import matplotlib.pyplot as plt

if __name__ == "__main__":
    TESTS = 2000
    x = np.arange(1, TESTS, 1)
    y = []
    for i in tqdm(x):
        # f = randomFib(i)
        # n = fib2dec(f)
        fibs = computeFibs(i)
        y.append(len(fibs))

    plt.plot(x, y)
    plt.show()