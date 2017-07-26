import operator
ver,edge = map(int,input().split(' '))
hash1 = {}
hash2 = {}
for _ in range(edge):
	v1,v2,weight = map(int,input().split(' '))
	hash1[v1,v2] = weight
	if hash2.get(v1,[]):
		hash2[v1].append(v2)
	else:
		hash2[v1]=[v2]
	if hash2.get(v2,[]):
		hash2[v2].append(v1)
	else:
		hash2[v2]=[v1]
source = int(input())
weights = 0
hash1 = sorted(hash1.items(),key=operator.itemgetter(1))
vertices_visited = []
print(hash1)
src_connct = [source]
for h in hash1:
	weightt = h[1]
	vert1 = h[0][0]
	vert2 = h[0][1]
	if (vert1 not in vertices_visited or vert2 not in vertices_visited) or len(src_connct)<ver:
		# print("....")
		weights+=weightt
		vertices_visited.append(vert1)
		vertices_visited.append(vert2)
		if source == vert1 and vert2 not in src_connct:
			src_connct.append(vert2)
			alls = hash2[vert2]
			for v in alls:
				if v not in src_connct:
					src_connct.append(v)
		if source == vert2 and vert1 not in src_connct:
			src_connct.append(vert1)
			alls = hash2[vert2]
			for v in alls:
				if v not in src_connct:
					src_connct.append(v)
	else:
		continue
	print(src_connct)
print(weights)

