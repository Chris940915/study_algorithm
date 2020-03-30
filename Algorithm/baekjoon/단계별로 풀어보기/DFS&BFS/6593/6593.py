import sys
from collections import deque

input_ = sys.stdin.readline


def bfs(s):
    queue = deque([s])
    visited[s[0]][s[1]][s[2]] = 0

    dx, dy, dz = [0,0,1,-1,0,0], [1,-1,0,0,0,0], [0,0,0,0,1,-1]

    while queue:
        z, x, y = queue.popleft()

        if x == exit_[1] and y == exit_[2] and z == exit_[0]:
            
            return 'Escaped in {} minute(s).'.format(visited[z][x][y])

        for idx in range(6):
            nx, ny, nz = x+dx[idx], y+dy[idx], z+dz[idx]

            if 0<=nz<l and 0<=nx<r and 0<=ny<c:
                if visited[nz][nx][ny] == -1 and matrix[nz][nx][ny] != '#':
                    visited[nz][nx][ny] = visited[z][x][y] + 1
                    queue.append([nz, nx, ny])
    return 'Trapped!'

while True:
    l, r, c = map(int, input_().split())

    if l == 0 and r == 0 and c == 0:
        break

    matrix = []
    visited = [[[-1]*c for _ in range(r)] for _ in range(l)]

    for f in range(l):
        temp_1 = []
        for i in range(r):
            temp_2 = list(input_().rstrip())
            for j in range(c):
                if temp_2[j] == 'S':
                    start_ = [f, i, j]
                if temp_2[j] == 'E':
                    exit_ = [f, i, j]
            temp_1.append(temp_2)
        pass_ = input_()
        matrix.append(temp_1)
    
    res = bfs(start_)
    print(res)
