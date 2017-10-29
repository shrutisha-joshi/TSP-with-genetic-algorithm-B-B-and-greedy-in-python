from random import randrange as rr

from math import sqrt     

def distance(l):
    s=0
    for i in range(1,len(l)):
        x1,y1=dic[l[i-1]][0],dic[l[i-1]][1]
        x2,y2=dic[l[i]][0],dic[l[i]][1]
        s+=sqrt((x2-x1)**2+(y2-y1)**2)
    return s

n_cities=int(input())
dic={}
for x in range(n_cities):
    dic[x+1]=tuple(list(map(int,input.strip().split())))
"""
dic={1:(16.47,96.10),
     2:(16.47,94.44),
     3:(20.09,92.54),
     4:(22.39,93.37),
     5:(25.23,97.24),
     6:(22.00,96.05),
     7:(20.47,97.02),
     8:(17.20,96.29),
     9:(16.30,97.38),
     10:(14.05,98.12),
     11:(16.53,97.38),
     12:(21.52,95.59),
     13:(19.41,97.13),
     14:(20.09,94.55)
     }"""

l=[(k+1) for k in range(14)]
cities=list(l)
len_c=len(cities)

population=len_c*10
# permutations

paths=[]
i=0
while i<population:
    r1=rr(1,len_c)
    r2=rr(1,len_c)
    while r1==r2:
        r1=rr(1,len_c)
        r2=rr(1,len_c)
    cities[r1],cities[r2]=cities[r2],cities[r1]
    if cities not in paths:
        paths.append(list(cities))
        i+=1

#crossovers
def crossover():
    j=0
    crossovers=[]
    parents=[]
    while j<population//2:
        r1=rr(0,population)
        r2=rr(0,population)
        
        parents.append(r1)
        parents.append(r2)
        while r1==r2 and r1 in parents and r2 in parents:
            r1=rr(0,population)
            r2=rr(0,population)
        p1=list(paths[r1])
        p2=list(paths[r2])
        
        r1=rr(1,len_c)
        r2=rr(1,len_c)
        while r1==r2:
            r1=rr(1,len_c)
            r2=rr(1,len_c)
        p1[r1:r2+1],p2[r1:r2+1]=p2[r1:r2+1],p1[r1:r2+1]

        xtra=list(set(l)-set(p1))
        len_x=len(xtra)
        for i in range(len(p1)):
            if p1.count(p1[i])>1:
                x=rr(0,len_x)
                p1[i]=xtra[x]
                del xtra[x]
                len_x-=1
                
        xtra=list(set(l)-set(p2))
        len_x=len(xtra)
        for i in range(len(p2)):
            if p2.count(p2[i])>1:
                x=rr(0,len_x)
                p2[i]=xtra[x]
                del xtra[x]
                len_x-=1
        
        if p1 not in crossovers and p2 not in crossovers and p1 not in paths and p2 not in paths:
            crossovers.append(list(p1))
            crossovers.append(list(p2))
            j+=1


    #mutation       
    mutations=[]
    i=0
    while i<(population):
        mutagens=list(crossovers[i])
        r1=rr(1,len_c)
        r2=rr(1,len_c)
        while r1==r2:
            r1=rr(1,len_c)
            r2=rr(1,len_c)
        mutagens[r1],mutagens[r2]=mutagens[r2],mutagens[r1]
        if mutagens not in paths and mutagens not in crossovers and mutagens not in mutations:
            mutations.append(list(mutagens))
            i+=1

    ultimatelist=paths+crossovers+mutations
    distances={}
    for i in range(len(ultimatelist)):
        distances[distance(ultimatelist[i])]=ultimatelist[i]
    
    
    dissort=sorted(distances.keys())
    print(dissort[0])
    for i in range(min(population,len(dissort))):
        paths[i]=distances[dissort[i]]
    

generations=int(input())
while generations>0:
    crossover()
    generations-=1
print(paths[0])

