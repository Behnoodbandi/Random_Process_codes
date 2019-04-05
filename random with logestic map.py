import numpy as np
import matplotlib
import time

x = np.random.rand(100)
y = np.zeros(100)
for i in range (len(x)):
    if 0.3 < x[i] < 0.8:
        y[i]=x[i]

print (x)
print (y)