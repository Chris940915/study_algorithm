import sys
from collections import deque

input_ = sys.stdin.readline

def bfs(a, b):

    queue = deque([[a, b, 0]])
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    visit[a][b][0] = 1

    while queue:
        x, y, z = queue.popleft()
        
        for i in range(4):
            n_x, n_y = dx[i]+x, dy[i]+y

            if 0<=n_x<n and 0<=n_y<m:
                if matrix[n_x][n_y] == 0 and visit[n_x][n_y][z] == -1:
                    visit[n_x][n_y][z] = visit[x][y][z]+1
                    queue.append([n_x, n_y, z])
                
                elif matrix[n_x][n_y] == 1 and z == 0 and visit[n_x][n_y][z] == -1:
                    visit[n_x][n_y][z+1] = visit[x][y][z]+1
                    queue.append([n_x, n_y, z+1])



n, m = map(int, input_().split())
matrix = []
for _ in range(n):
    matrix.append(list(map(int, list(input_().rstrip()))))

visit = [[[-1]*2 for _ in range(m)] for _ in range(n)]

bfs(0, 0)


if visit[n-1][m-1][0] == -1:
    print(visit[n-1][m-1][1])
elif visit[n-1][m-1][1] == -1:
    print(visit[n-1][m-1][0])
else:
    print(min(visit[n-1][m-1]))