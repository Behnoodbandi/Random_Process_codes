import numpy as np
from astropy.io import fits
import random
import matplotlib.pyplot as plt

hdulist = fits.open('test.fit')

data = hdulist[0].data


plt.imshow(data.T, cmap=plt.cm.viridis)
plt.colorbar()
plt.show()

print('FITS file opened')


N=10**7
X,Y = len(data[0,:]),len(data[:,0])

print('data size: ',X,Y)
print('flip coins...')

rx = np.random.randint(0,X,N)
ry = np.random.randint(0,Y,N)

total = 0
sun = 0

print('estimating area')

for i in range (0,N):
    x,y = rx[i],ry[i]
    if data[y][x] > 50:
        sun += 1
    total += 1
print(total,sun)

s_sun = X*Y*(sun/total)
print (s_sun)
plt.imshow(data, cmap=plt.cm.viridis)
plt.colorbar()
plt.show()
