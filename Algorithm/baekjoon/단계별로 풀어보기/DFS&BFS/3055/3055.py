from collections import deque


def water_bfs(water, goal):
    queue = deque(water)

    for w in water:
        water_path[w[0]][w[1]] = 1

    dx, dy = [0,0,1,-1], [1,-1,0,0]

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx, ny = dx[i]+x, dy[i]+y

            if 0<=nx<c and 0<=ny<r:
                if not [nx, ny] in rocks and [nx, ny] != goal and water_path[nx][ny] == 0:
                    water_path[nx][ny] = water_path[x][y] + 1
                    queue.append([nx, ny])

def d_bfs(start, goal):
    queue = deque()
    queue.append([start[0], start[1]])

    d_path[start[0]][start[1]] = 1

    dx, dy = [0,0,1,-1], [1,-1,0,0]

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx, ny = dx[i]+x, dy[i]+y

            if 0<=nx<c and 0<=ny<r:
                if not [nx, ny] in rocks and d_path[nx][ny] == 0:
                    if water_path[nx][ny] == 0 or d_path[x][y]+1 < water_path[nx][ny]:
                        d_path[nx][ny] = d_path[x][y] + 1
                        queue.append([nx, ny])
       
c, r = map(int, input().split())
rocks = []
water_path = [[0]*r for _ in range(c)]
d_path = [[0]*r for _ in range(c)]
water = []
for i in range(c):
    enter = list(input())
    for j in range(r):
        
        if enter[j] == 'X':
            rocks.append([i,j])
        if enter[j] == 'D':
            goal = [i,j]
        if enter[j] == 'S':
            start = [i,j]
        if enter[j] == '*':
            water.append([i,j])
            water_path[i][j] = 1
water_bfs(water, goal)
d_bfs(start, goal)

if d_path[goal[0]][goal[1]] == 0:
    print('KAKTUS')
else:
    print(d_path[goal[0]][goal[1]]-1)

