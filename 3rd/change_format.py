change = [500,100,50,10,5,1]
tally = int(input())
tally = 1000 - tally
for i in range(6):
    if(tally//change[i]):
        print(str(change[i]) + ", "+str(tally//change[i])+";", end=' ')
    tally %= change[i]