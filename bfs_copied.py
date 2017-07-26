def BFS (arg,graph,visited):
    #print(g.graph)
    visited[arg] = 0
    queue = []
    queue.append(arg)
    while queue :
        arg = queue.pop(0)
        #queue.pop(0)
        for j in graph[arg] :
            if visited[j] == -1 :
                visited[j] = visited[arg] + 1
                queue.append(j)
        
for __ in range (int(input())): 
    n,m = [int(z) for z in input().split()]
    graph = {}
    visited=[-1]*(n+1)
    for i in range (1,n+1):
        graph[i]=[]
    for i in range (m):
        num1 , num2 = [int(zz) for zz in input().split()]
        graph[num1].append(num2)
        graph[num2].append(num1)
    A = int(input())
    
    
    BFS(A,graph,visited)
    for distance in visited[1::] :
            if distance == -1 :
                print (-1, end = " ")
            elif distance != 0 :
                print (distance*6 , end = " ")
    print ()