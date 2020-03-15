tmpstr = input()
tmplst = tmpstr.split()
n,p,d = int(tmplst[0]), int(tmplst[1]), int(tmplst[2])
x, y, population = [0] * n, [0] * n, [0] * n
has = [0] * n
for i in range(n):
    tmpstr = input()
    tmplst = tmpstr.split()
    x[i], y[i], population[i] = int(tmplst[0]), int(tmplst[1]), int(tmplst[2])
#iterate p times to set
for k in range(p):
    max, which = 0, 0
    #iterate through each cities
    for i in range(n):
        cnt = 0
        for j in range(n):
            if((x[i]-x[j])**2 + (y[i] - y[j])**2 <= d * d):
                if(not(has[j])):
                    cnt += population[j]
        if cnt > max:
            max = cnt
            which = i
    for i in range(n):
        if((x[i]-x[which])**2 + (y[i] - y[which])**2 <= d * d):
            has[i] = 1
    #print(k, max, which)
    print(which + 1, end = ' ')
sum = 0
for i in range(len(has)):
    if(has[i]):
        sum += population[i]
print(sum)