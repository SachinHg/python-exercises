def find(parent,ver):
	if parent[ver] == ver:
		return ver
	return find(parent,parent[i])

def union(parent,rank,x,y):
	root1 = find(parent,x)
	root2 = find(parent,y)
	if root1 < root2:
		parent[root1] = root2
	elif root2 < root1:
		parent[root2] = root1
	else:
		parent[root1] = root2
		rank[root2]+=1

graph = []
ver,edges = map(int,input().split(' '))
for _ in range(edges):
	ver1,ver2,weight = map(int,input().split(' '))
	graph.append([ver1-1,ver2-1,weight])
res = []
i = 0
e = 0
graph = sorted(graph,key=lambda item: item[2])
parent = []
rank = []
for node in range(ver):
	parent.append(node)
	rank.append(0)
while e < ver-1:
	v1,v2,w = graph[i]
	i+=1
	x = find(parent,v1)
	y = find(parent,v2)
	if x != y:
		e+=1
		res.append(w)
		union(parent,rank,x,y)
print(sum(res))