n = int(input("Num of jobs: "))
m = int(input("Num of machines: "))
pSTR = input("Processing times: ")

processes = pSTR.split()
machines = [0] * m
order = [0] * n
for i in range(n):
    processes[i] = int(processes[i])
processes.sort(reverse = True)

#iterate through each jobs
for i in range(n):
    min, which = 1000000, 0
    #iterate through each machines workload and find the minimun one currently
    for j in range(m):
        if machines[j] < min :
            min, which = machines[j], j
    #test
    #print(min, which)
    machines[which] += processes[i]
    order[i] = which

print(machines)
print(order)

