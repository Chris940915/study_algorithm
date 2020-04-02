import sys

n = int(input())
m = int(input())

max_v = sys.maxsize

matrix = [[max_v]*(n) for _ in range(n)]

for _ in range(m):
    a, b, c = map(int, input().split())
    matrix[a-1][b-1] = min(c, matrix[a-1][b-1])

for k in range(n):
    for i in range(n):
        for j in range(n):
            if i==j:
                matrix[i][j] = 0
            else:
                matrix[i][j] = min(matrix[i][j], matrix[i][k] + matrix[k][j])

for m in matrix:
    print(*m)