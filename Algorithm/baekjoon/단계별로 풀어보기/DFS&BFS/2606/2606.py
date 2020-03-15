def solution(graph, start):
    visit = [start]
    queue = [start]
    count = 0

    while queue:
        node = queue.pop(0)

        for search_node in range(len(graph[node])):
            if graph[node][search_node] and search_node not in visit:
                count += 1
                visit.append(search_node)
                queue.append(search_node)
    return count



if __name__ == "__main__":
    n = int(input())
    m = int(input())

    matrix = [[0]*(n+1) for _ in range(n+1)]

    for _ in range(m):
        a, b = map(int, input().split())
        matrix[a][b] = 1
        matrix[b][a] = 1

    answer = solution(matrix, 1)
    print(answer)