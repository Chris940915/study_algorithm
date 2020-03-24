from collections import deque

def bfs(visit, n, m, h):
# h, n, m 
    visit = deque(visit)

    dx, dy, dz = [0, 0, 1, -1, 0, 0], [1, -1, 0, 0, 0, 0], [0, 0, 0, 0, 1, -1]
    count = -1
    while visit:
        count += 1
        for _ in range(len(visit)):
            x, y, z = visit.popleft() 

            for i in range(6):
                nx, ny, nz = dx[i]+x, dy[i]+y, dz[i]+z

                if 0<=nx<n and 0<=ny<m and 0<=nz<h:
                    if matrix[nz][nx][ny] == 0:
                        matrix[nz][nx][ny] = 1
                        visit.append([nx, ny, nz])
    for m in matrix:
       for m_ in m:
            if 0 in m_:
                return -1
    return count


m, n, h = map(int, input().split())
matrix = []
visit = []

for k in range(h):
    enter_ = []
    for i in range(n):
        enter = list(map(int, input().split()))

        for j in range(m):
            if enter[j] == 1:
                visit.append([i, j, k])
        enter_.append(enter)
    matrix.append(enter_)

res = bfs(visit, n, m, h)
print(res)