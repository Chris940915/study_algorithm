from collections import deque

def group_check(a, b):
    queue = deque()
    queue.append([a,b])
    visit = [[0]*6 for _ in range(12)]

    visit[a][b] = 1
    coordinates = [[a,b]]

    dx, dy = [0,0,1,-1], [1,-1,0,0]

    while queue:

        x, y = queue.popleft()

        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]

            if 0<=nx<12 and 0<=ny<6:
                if matrix[nx][ny] == matrix[x][y] and visit[nx][ny] == 0:
                    visit[nx][ny] = visit[x][y]
                    queue.append([nx, ny])
                    coordinates.append([nx, ny])
    
    return coordinates
    
def move():
    for y in range(6):
        for x in range(11, -1, -1):
            if matrix[x][y] == '.':
                continue
            for k in range(11, x, -1):
                if matrix[k][y] == '.':
                    matrix[k][y] = matrix[x][y]
                    matrix[x][y] = '.'

matrix = []
for _ in range(12):
    enter = list(input())
    matrix.append(enter)

answer = 0
while True:
    groups = []
    check = 0
    for i in range(12):
        for j in range(6):
            if matrix[i][j] != '.':
                res = group_check(i, j)

                if len(res) >= 4:
                    check += 1
                    for r in res:
                        matrix[r[0]][r[1]] ='.'

    move()


    if check > 0:
        answer += 1
    else:
        break

print(answer)