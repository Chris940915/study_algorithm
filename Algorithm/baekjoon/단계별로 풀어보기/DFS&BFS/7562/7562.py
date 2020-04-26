from collections import deque

t = int(input())

def bfs(start, goal, graph, n):
    q = deque([start])
    graph[start[0]][start[1]] = 0

    while q:
        x, y = q.popleft()

        if x == goal[0] and y == goal[1]:
            return graph[x][y]

        for i in range(8):
            nx, ny = x+dx[i], y+dy[i]

            if 0<= nx < n and 0<= ny < n and graph[nx][ny] == -1:
                graph[nx][ny] = graph[x][y] + 1
                q.append([nx, ny])

res = []

for _ in range(t):
    i = int(input())
    matrix = [[-1]*i for _ in range(i)]
    
    a, b = map(int, input().split())
    x, y = map(int, input().split())

    dx, dy = [2, 2, 1, 1, -1, -1, -2, -2], [1, -1, 2, -2, 2, -2, 1, -1]

    res.append(bfs([a,b], [x,y], matrix, i))

for r in res:
    print(r)