import numpy as np

#N = int(input('تعداد انداختن سکه چند بار باشد؟'))
N = 1000000000
X = np.random.randint(1,3,N)
shir,khat=0,0
for i in range (0,len(X)):
    if X[i] == 1:
        shir = shir +1
    else:
        khat = khat +1
if N==1:
    if shir == 1 :
        print('شیر')
    else:
        print('خط')
else:
    print ('شیر' , shir)
    print ('خط' , khat)
    if shir > khat:
        print('شیر')
    else:
        print('خط')
