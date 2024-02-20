def filterOutliers(x, y):
    CUTOFF = 1.2
    n = 25
    # Filter out if any element is greater than CUTOFF times average of the previous n elements
    # or less than CUTOFF-1 times the average of the previous n elements
    x_new = []
    y_new = []
    for i in range(len(y)):
        if i < n:
            x_new.append(x[i])
            y_new.append(y[i])
        else:
            avg = sum(y[i-n:i])/n
            if y[i] > CUTOFF*avg or y[i] < (CUTOFF-1)*avg:
                continue
            x_new.append(x[i])
            y_new.append(y[i])
    return x_new, y_new

def smooth(x, y, alpha=0.5):
    # Smooth out graph using expontential moving average
    smoothed = []
    last = y[0]
    for i in range(len(y)):
        smoothed.append(last*alpha + (1-alpha)*y[i])
        last = smoothed[-1]
    return x, smoothed

def removeSpikes(x, y):
    pass