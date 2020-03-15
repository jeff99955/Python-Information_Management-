import math

k=9E9
e=1.6E-19
z = 2
v = 1.5E5
m = 9.1E-31

print(k*e*e/((3/2)*m*v*v))

def ln(x):
    return math.log(x+math.sqrt(1/16+x*x))

print("%E"%(k * (ln(1) - ln(1/4)) * 1E-6))
"""
d=0.17

def F(x):
     return 2*k*2*e*4*e*x/math.pow(d*d+x*x, 3/2)

max , which = 0.0, 0.0
for i in range (501):
    res = F(i/100)
    if res > max:
        max = res
        which = i/100

print(max, which)


def F(x):
    return 1 - (z/math.sqrt(z*z+x*x))

print(F(1/2) / F(1))

p = 3.02E-25
E = 46

print(p*E*(math.cos(203*2*math.pi/360) - math.cos(23*2*math.pi/360)))
"""