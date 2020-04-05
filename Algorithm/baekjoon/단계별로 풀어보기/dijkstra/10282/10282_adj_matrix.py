import sys
input = sys.stdin.readline

INF = sys.maxsize

def solution(k, s, graph):
    visit = [False] * k
    distance = [INF] * k
    distance[s] = 0
    while True:
        n = -1
        m = INF

        for j in range(k):
            if not visit[j] and m > distance[j]:
                m = distance[j]
                n = j
        if m == INF:
            break

        visit[n] = True

        for j in range(k):
            if visit[j]: continue
            via = distance[n] + graph[n][j]
            if via < distance[j]:
                distance[j] = via
    return distance


T = int(input())

for _ in range(T):
    n, d, c = map(int, input().split())
    
    matrix = [[INF]*n for _ in range(n)]
    mapping = dict()

    for _ in range(d):
        a, b, s = map(int, input().split())
        matrix[b-1][a-1] = s
        
        if b-1 in mapping:
            values = mapping[b-1]
            values.append(a-1)
            mapping[b-1] = values
        else:
            mapping[b-1] = [a-1]
    temp = []
    for k, values in mapping.items():
        result = solution(n, k, matrix)
        #print(values)
        for v in values:
            temp.append(result[v])
    print(len(temp), max(temp))


