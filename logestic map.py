import random
import matplotlib as plt
import numpy as np
import math
x=np.zeros(100)
x[0]=0.1
y=list(range(0, 100))
mu=3.8
i=0
while(i<99):
        x[i+1]=mu*x[i]*(1-x[i])
        i+=1
print (x)
np.savetxt("logestic1.csv", x, delimiter=",")
plt.plot(y,x)
plt.show()