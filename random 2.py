import random
n = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
N = 900000
i, j = 0, 0
while i < N:
    a = random.randint(0, 10)
    n[a] = n[a] + 1
    i = i + 1

while j < 11:
    n[j] = n[j] / N
    j = j + 1
i,j=0,0
print('For', N, 'random:')
print(n)
fluc = max(n) - min(n)
print('Fluc=', fluc)
