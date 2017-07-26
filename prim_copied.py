from collections import defaultdict
import heapq
ver,edges = map(int,input().split(' '))
hash1 = defaultdict(list)
init =[]
total_weight = 0
for _ in range(edges):
    ver1,ver2,weight = map(int,input().split(' '))
    hash1[ver1].append((ver2,weight))
    hash1[ver2].append((ver1,weight))
start = int(input())
connected = [0]*ver
heapq.heappush(init,(0,1))
heapq.heapify(init)
while init:
    v = heapq.heappop(init)
    if connected[v[1]-1] == 0:
        connected[v[1]-1] = 1
        total_weight+=v[0]
        for vv in hash1[v[1]]:
            heapq.heappush(init,(vv[1],vv[0]))
print(total_weight)