""" 

    다른 분들의 코드를 보고 깨달았다.
    내가 짠 코드는 정답은 맞추지만 시간 초과가 뜬다....
    그러므로 틀린 코드다 

    블로그에 적어놓으신대로 얼마나 내가 머리가 굳어져있는지 알 수 있었다...

    플로이드는 모든 정점에서 모든 정점까지의 최소거리를 구해준다.

    갈 수 있는 정점사이를 0으로 놓고 갈 수 없는 정점사이를 1로 놓고 계산을 + 로 한다면
    양방향 그래프를 만들어야하는 최소한의 개수를 알 수 있게 된다.
"""


import sys
input = sys.stdin.readline
INF = sys.maxsize

def solution(s, g, graph):
    
    if s == g:
        return 0

    if graph[s][g] == 0:
        return 0

    for k in range(n):
        for i in range(n):
            for j in range(n):
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

    return graph[s][g]


n, m = map(int, input().split())

# 전체를 INF 값으로 놓는다.
matrix = [[INF]*n for _ in range(n)]

for _ in range(m):
    u, v, b = map(int, input().split())

    if b == 0:
        matrix[u-1][v-1] = 0
        matrix[v-1][u-1] = 1
    else:
        matrix[u-1][v-1] = 0
        matrix[v-1][u-1] = 0

k = int(input().rstrip())

for _ in range(k):
    q, w = map(int, input().split())
    res = solution(q-1, w-1, matrix)
    print(res)