graph = {
        '1': ['2', '3', '4'],
        '2': ['5', '6'],
        '5': ['9', '10'],
        '4': ['7', '8'],
        '7': ['11', '12']
        }

def bfs(graph, start):
    visited[start] = 0
    queue = []
    queue.append([start])
    while queue:
        path = queue.pop(0)
        # node = path[-1]
        # if node == end:
        #     return path
        for adjacent in graph.get(node, []):
            if visited[adjacent] == -1:
                visited[adjacent] = visited[node]+1
                queue.append(j)
            # new_path = list(path)
            # new_path.append(adjacent)
            # queue.append(new_path)
    return visited

print (bfs(graph,'1'))