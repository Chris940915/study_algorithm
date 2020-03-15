def dfs(graph, start, visit):
    visit += [start]

    for search in range(len(graph[start])):
        if graph[start][search] and search not in visit:
            visit = dfs(graph, search, visit)

    return  visit



def bfs(graph, start):
    visit = [start]
    queue = [start]

    while queue:
        node = queue.pop(0)

        for search in range(len(graph[node])):
            if graph[node][search] and search not in visit:
                visit.append(search)
                queue.append(search)
    return visit




if __name__ == "__main__":
    n, m, v = map(int, input().split())

    matrix = [[0]*(n+1) for _ in range(n+1)]

    for _ in range(m):
        a, b = map(int, input().split())
        matrix[a][b] += 1
        matrix[b][a] += 1
    
    dfs_answer = dfs(matrix, v, [])
    print(*dfs_answer)
    bfs_answer = bfs(matrix, v)
    print(*bfs_answer)