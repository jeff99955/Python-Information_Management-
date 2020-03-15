""" num = 5
dst = [[0,9,6,7,4],
    [9,0,5,9,6],
    [6,5,0,3,1],
    [7,9,3,0,4],
    [4,6,1,4,0]] """

num = int(input())
dst = []
for i in range(num):
    dst.append(input().split())
    for j in range(num):
        dst[i][j] = int(dst[i][j])
# dst[i][j] is the distance between i, j

origin = 0
tourlen = 0
tour = [origin]
unvisited = []
for i in range(num):
    unvisited.append(i)
unvisited.remove(origin)

cur = origin
for i in range(num - 1):
    next = -1
    min = 100000000
    for j in unvisited:
        if dst[cur][j] < min:
            next = j
            min = dst[cur][j]
    unvisited.remove(next)
    tour.append(next)
    tourlen += min
    cur = next

tour.append(origin)
tourlen += dst[cur][origin]

print(tourlen, tour)