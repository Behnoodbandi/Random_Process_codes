import numpy as np
import matplotlib as plt
import random
import math

def logestic (mu,n,x0):
    i=0
    x=x0
    while i<=n:
        x=mu*x*(1-x)
        i+=1
    return x
mu = np.arange(3, 4.01, 0.01)
n=5
x0 = 0.1
x = np.zeros(102)
i=0

while(i<100):
        x[i]=logestic(mu[i],n,x0)
        i+=1

np.savetxt("logestic.csv", x, delimiter=",", fmt='%s')
np.savetxt("mu.csv",mu,delimiter=",", fmt='%s')
