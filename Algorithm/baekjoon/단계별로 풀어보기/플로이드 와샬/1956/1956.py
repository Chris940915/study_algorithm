

# 자기 자신의 점으로 돌아오는 플로이드 와샬.
# 플로이드 와샬 진행 중 자기자신을 건너뛰지않고 저장해놓으면 쉽게 풀 수 있다.

import sys

INF = sys.maxsize

v, e = map(int, input().split())

matrix = [[INF]*v for _ in range(v)]

for _ in range(e):
    a, b, c = map(int, input().split())
    matrix[a-1][b-1] = c

for k in range(v):
    for i in range(v):
        if matrix[i][k] == INF: continue 
        for j in range(v):
            if matrix[k][j] != INF:
                matrix[i][j] = min(matrix[i][j], matrix[i][k] + matrix[k][j])
answer = []

min_V = INF

for i in range(v):
    min_V = min(min_V, matrix[i][i])

if min_V == INF:
    print(-1)
else:
    print(min_V)    