def bfs(graph, start,target):
	queue = []
	chk = []
	queue.append(start)
	path = -1
	cnt = 0
	# print(graph)
	while len(queue) > 0:
		#print("<<<>>>>>")
		if target not in queue:
			cnt+=1
		v = queue.pop(0)
		if v == target:
			return cnt
		elif v not in chk:
			# cnt+=1
			for e in graph[v]:
				if v not in chk:
					queue.append(e)
			# cnt+=1
			chk.append(v)
		#cnt+=1
	return -1
    
t = int(input())
for _ in range(t):
	v_hash = {}
	v,e = list(map(int,input().split(' ')))
	for __ in range(e):
		v1,v2 = list(map(int,input().split(' ')))
		# v_hash[v1] = []
		# v_hash[v2] = []
		if v1 in v_hash:
			v_hash[v1].append(v2)
		else:
			v_hash[v1] = [v2]
		if v2 in v_hash:
			v_hash[v2].append(v1)
		else:
			v_hash[v2] = [v1]
	
	start = int(input())
	targets = []
	targets = list(range(1,v+1))
	targets.remove(start)
	distances = []
	for t in targets:
		#print("///////")
		dist = bfs(v_hash,start,t)
		distances.append(dist)
	#print(bfs(v_hash,start,4))
	distances = [x*6 if x>-1 else x for x in distances]
	distances = map(str,distances)
	print(' '.join(distances))