import numpy as np
import time
import matplotlib.pyplot as plt
import random

def fix_format(s1, s2):
    s1 = [0] + s1
    s2 = [0] + s2
    prev = s1[0]
    for i in range(1, len(s1)):
        if prev == 1 and s1[i] == 1:
            s1[i-2] = 1
            s1[i-1] = 0
            s1[i] = 0
        prev = s1[i]
    prev = s2[0]
    for i in range(1, len(s2)):
        if prev == 1 and s2[i] == 1:
            s2[i-2] = 1
            s2[i-1] = 0
            s2[i] = 0
        prev = s2[i]
    return s1, s2


def to_arr_pad(s1, s2):
    if len(s1) < len(s2):
        diff = len(s2) - len(s1)
        s1 = [0] * diff + s1
    if len(s2) < len(s1):
        diff = len(s1) - len(s2)
        s2 = [0] * diff + s2
    s1 = s1[::-1]
    s2 = s2[::-1]
    s1.append(0)
    s1.append(0)
    s2.append(0)
    s2.append(0)
    return s1, s2
    

def add(s1, s2):
    s1, s2 = fix_format(s1, s2)
    s1, s2 = to_arr_pad(s1, s2)
    # print(s1, s2)
    ans = [0] * len(s1)
    unsolved = True
    count = 0
    for i in range(len(s1)):
        ans[i] += s1[i] + s2[i]
    while unsolved:
        count += 1
        # TODO print(ans)
        for i in range(len(s1)):
            if ans[i] > 1:
                if ans[i] == 2:
                    # quotient = int(ans[i]/2)
                    # remainder = ans[i] % 2
                    quotient = 1
                    remainder = 0
                    ans[i] = remainder
                    if i == 0:
                        ans[1] += quotient
                    elif i == 1:
                        ans[2] += quotient
                        ans[0] += quotient
                    else:
                        ans[i+1] += quotient
                        ans[i-2] += quotient
                elif ans[i] == 3:
                    # quotient = int(ans[i]/3)
                    quotient = 1
                    remainder = 0
                    # remainder = ans[i] % 3
                    ans[i] = remainder
                    if i == 0:
                        ans[2] += quotient
                    elif i == 1:
                        ans[3] += quotient
                        ans[0] += quotient
                    else:
                        ans[i+2] += quotient
                        ans[i-2] += quotient
                else:
                    raise ValueError(f"value was greater than 3, {ans[i]}, answer was {ans}")

                
                # ans = update_ans(i, ans)
        # print(ans)
        if any(val not in (0, 1) for val in ans):
            unsolved = True
        else:
            unsolved = False
    return ans[::-1], count

def randomFib(length):
    arr = []
    for i in range(length):
        arr.append(random.choice([0, 1]))
    return arr



if __name__ == "__main__":
    # print(add("1110", "1110"))
    s1 = "111100"
    s2 = "10011010"
    # print(add(s1, s2))
    x = np.arange(1, 10000, 1)
    y = []
    for i in x:
        print(i)
        a = randomFib(i)
        b = randomFib(i)
        (a, b)
        start = time.time()
        ans, count = add(a, b)
        # TODO print(ans[::-1])
        y.append(count)
        # y.append(time.time() - start)
    plt.plot(x[1:], y[1:])
    slope, intercept = np.polyfit(x, y, 1)
    print("slope", slope)
    print("intercept", intercept)
    log_x = np.log(x)
    log_y = np.log(y)

    # Calculate the coefficients of the linear regression line on the log-transformed data
    slope_log, intercept_log = np.polyfit(log_x, log_y, 1)
    print("log slope", slope_log)
    print("intercept slope", intercept_log)
    plt.show()
    print("Done")
    


"""
notes:
- need to prove that the sum of any two numbers in base fibonacci won't overflow more than two spaces"""
