# 輸入 n p d
# 並將其分隔為list
npd = input("Please input n p d: ")
npdsz = npd.split()

# 將npd的list換成int
npd_sz = [0] * len(npdsz)
for i in range(len(npdsz)):
    npd_sz[i] = int(npdsz[i])
   
# 輸入coordinate + population
coor_p = []
for b in range(npd_sz[0]):
    cp = input("Please input coordinate + population: ")
    coor_p.append(cp)

# 將coordinate + population 轉成二維的list    
for x in range(npd_sz[0]):
    coor_p[x] = coor_p[x].split()

    for y in range(len(coor_p[x])):
        coor_p[x][y] = int(coor_p[x][y])

#製造一個有元素為0的二維數組
import math
   
distance = []
for x in range(npd_sz[0]):
    distance.append([])
    for y in range(npd_sz[0]):
        distance[x].append(0)

#創造一個叫做distance的數組用於記錄兩地之間的距離       
for x in range(npd_sz[0]):
    for y in range(npd_sz[0]):
        distance[x][y] =  math.sqrt((coor_p[x][0] - coor_p[y][0]) ** 2 + ((coor_p[x][1] - coor_p[y][1]) ** 2))


#
city_1 = 0
city = []
population_2 = 0
for z in range(npd_sz[1]):     #進行基地台數目次的循環
    population_ALL = 0         #重置population_ALL，以避免影響下面的運算
    for x in range(npd_sz[0]):                    
        population_1 = 0                         #   
        for y in range(npd_sz[0]):               #
            if distance[x][y] <= npd_sz[2]:      #尋找基地台  
                population_1 += coor_p[y][2]     #
                                                 #
        if population_1 > population_ALL:        #  
            population_ALL = population_1        #
            city_1 = x                           #
    
    for y in range(npd_sz[0]):        
        if distance[city_1][y] <= npd_sz[2]:     #
            population_2 += coor_p[y][2]         #基地台覆蓋的城鎮的人口變為0
            coor_p[y][2] = 0                     #
    
    city.append(city_1 + 1)

#輸出
for i in range(len(city)):
    print(city[i], end=" ")
print(population_2)