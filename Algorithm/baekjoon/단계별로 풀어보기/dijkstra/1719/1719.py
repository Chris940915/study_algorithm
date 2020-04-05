import heapq
import sys

input = sys.stdin.readline
INF = sys.maxsize

def solution(k, s, graph):
    q = []
    heapq.heappush(q, [0, s])

    distance = [INF] * k
    distance[s] = 0

    while q:
        c, p = heapq.heappop(q)
    
        for pos, cost in graph[p]:
            cost += c

            if cost < distance[pos] :
                distance[pos] = cost
                heapq.heappush(q, [cost, pos])
                d[pos][s] = p+1

n, m = map(int, input().split())
matrix = [[] for _ in range(n)]
d = [[0] * n for _ in range(n)]

for _ in range(m):
    a, b, c = map(int, input().split())
    matrix[a-1].append([b-1, c])
    matrix[b-1].append([a-1, c])


for i in range(n):
    solution(n, i, matrix)


for i in range(n):
    for j in range(n):
        if i == j:
            print("-", end=" ")
        else:
            print(d[i][j], end=" ")
    print()
