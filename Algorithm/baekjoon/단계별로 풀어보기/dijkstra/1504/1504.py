import sys

INF = sys.maxsize

# 방향성이 없는 그래프. 
# 정점 2개를 지나야하는데 어떤 정점을 먼저 지나야하는지에 대한 언급이 따로 없다. 


def dijkstra(start, goal, n, graph):
    distance = [INF] * n
    distance[start] = 0
    visit = [False] * n

    while True:
        k = -1
        m = INF

        for j in range(n):
            if m > distance[j] and not visit[j]:
                m = distance[j]
                k = j
        
        if m == INF:
            break
        
        visit[k] = True

        for j in range(n):
            if visit[j]:
                continue
            via = distance[k] + graph[k][j]
            if via < distance[j]:
                distance[j] = via
    return distance[goal]

n, e = map(int, input().split())
matrix = [[INF]*n for _ in range(n)]

for _ in range(e):
    a, b, c = map(int, input().split())
    matrix[a-1][b-1] = c
    matrix[b-1][a-1] = c

mid_1, mid_2 = map(int, input().split())

answer_1 = 0
answer_2 = 0
a_1 = [0, mid_1-1, mid_2-1]
b_1 = [mid_1-1, mid_2-1, n-1]

for a_, b_ in zip(a_1, b_1):
    temp = dijkstra(a_, b_, n, matrix)
    if temp == INF:
        answer_1 = -1
        break
    else:
        answer_1 += temp
a_2 = [0, mid_2-1, mid_1-1]
b_2 = [mid_2-1, mid_1-1, n-1]


for a_, b_ in zip(a_2, b_2):
    temp = dijkstra(a_, b_, n, matrix)
    if temp == INF:
        answer_2 = -1
        break
    else:
        answer_2 += temp

print(min(answer_1, answer_2))



