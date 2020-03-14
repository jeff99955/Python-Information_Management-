import array as arr
import math
ar = arr.array('f', [])
c = int(input())
r = int(input())
N = int(input())
q = int(input())

for i in range(N+1):
    ar.append(float(input()))

sum = float()
left = float()

for i in range(q):
    #print("%d %d %f"%(r, c, ar[i]), end = ' ')
    sum += ar[i] * (r * i - c*q)
    left += ar[i]
    #print("%f"%sum)
sum += (1-left) * (r*q-c*q)
print(sum)