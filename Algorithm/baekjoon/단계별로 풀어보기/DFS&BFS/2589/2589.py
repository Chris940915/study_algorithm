from collections import deque
import sys

input_ = sys.stdin.readline

n, m = map(int, input_().split())
matrix = []
visit = [[-1]*m for _ in range(n)]

for i in range(n):
    matrix.append(list(input_().rstrip()))

count = 0
max_d = 0

def bfs(start):
    global max_d

    queue = deque()
    queue.append(start)

    dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]
    visit[start[0]][start[1]] = count
    distance = 0

    while queue:
        distance += 1
        for _ in range(len(queue)):
            x, y = queue.popleft()

            for i in range(4):
                nx, ny = dx[i]+x, dy[i]+y

                if 0<=nx<n and 0<=ny<m:
                    if matrix[nx][ny] == 'L' and visit[nx][ny] < count:
                        visit[nx][ny] = count
                        queue.append([nx, ny])
    distance -= 1

    max_d = max(max_d, distance)
    
    return max_d

for i in range(n):
    for j in range(m):
        if matrix[i][j] == 'L':
            count += 1
            bfs([i,j])   
print(max_d)


