import array as arr
import math
ar = arr.array('f', [])
c = int(input())
r = int(input())
N = int(input())
s = int(input())

max = float()
which = 0
for i in range(N+1):
    ar.append(float(input()))

for q in range(N+1):   
    sum = float()
    left = float()
    for i in range(q):
        #print("%d %d %d %f"%(q,r, c, ar[i]), end = ' ')
        sum += ar[i] * (r * i - c*q + (q - i)*s)
        left += ar[i]
        #print("%f"%sum)
    sum += (1-left) * (r*q-c*q)
    print(q, sum)
    if sum > max:
        max = sum
        which = q
print(which, max)