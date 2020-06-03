from collections import deque
import sys

input = sys.stdin.readline
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(x, y, dir):
    q.append([x, y, dir])
    c[x][y][dir] = 1
    while q:
        x, y, dir = q.popleft()
        if x == x1-1 and y == y1-1 and dir == dir1-1:
            print(c[x][y][dir]-1)
            return
        turn_r(x, y, dir)
        turn_l(x, y, dir)
        nx = x + dx[dir]
        ny = y + dy[dir]
        if 0 <= nx < m and 0 <= ny < n:
            if a[nx][ny] == 0:
                move(x, y, dir)
        else:
            turn_l(x, y, dir)
            turn_r(x, y, dir)

def move(x, y, dir):
    cnt = 1
    nx = x; ny = y
    while cnt <= 3:
        nx += dx[dir]
        ny += dy[dir]
        if nx < 0 or ny < 0 or nx >= m or ny >= n or a[nx][ny] == 1:
            return
        if c[nx][ny][dir] == 0:
            c[nx][ny][dir] = c[x][y][dir] + 1
            q.append([nx, ny, dir])
        cnt += 1


def turn_r(x, y, dir):
    if dir == 0: ndir = 2
    elif dir == 1: ndir = 3
    elif dir == 2: ndir = 1
    else: ndir = 0
    if c[x][y][ndir] == 0:
        c[x][y][ndir] = c[x][y][dir] + 1
        q.append([x, y, ndir])

def turn_l(x, y, dir):
    if dir == 0: ndir = 3
    elif dir == 1: ndir = 2
    elif dir == 2: ndir = 0
    else: ndir = 1
    if c[x][y][ndir] == 0:
        c[x][y][ndir] = c[x][y][dir] + 1
        q.append([x, y, ndir])

m, n = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(m)]
x0, y0, dir0 = map(int, input().split())
x1, y1, dir1 = map(int, input().split())

c = [[[0]*4 for _ in range(n)] for _ in range(m)]
q = deque()

bfs(x0-1, y0-1, dir0-1)