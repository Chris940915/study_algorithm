import sys
from collections import deque

input_ = sys.stdin.readline


# 시간초과 났던 코드
# 따로 저장을 한다. 

def make_rect(a, b, c, d):
    for x in range(b, d):
        for y in range(a, c):
            rect_list.append([x,y])


def bfs(i, j):
    queue = deque([[i,j]])
    visit[i][j] = True
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    count = 1

    while queue:
        x, y = queue.popleft()

        for idx in range(4):
            n_x, n_y = dx[idx]+x, dy[idx]+y

            if 0<=n_x<m and 0<=n_y<n:
                if [n_x, n_y] not in rect_list and not visit[n_x][n_y]:
                    count += 1
                    visit[n_x][n_y] = True
                    queue.append([n_x, n_y])
    return count

m, n, k = map(int, input_().split())

rect_list = []
visit = [[False]*n for _ in range(m)]

for _ in range(k):
    a, b, c, d = map(int, input_().split())
    make_rect(a, b, c, d)

result = []

for i in range(m):
    for j in range(n):
        if [i,j] not in rect_list and not visit[i][j]:
            count_ = bfs(i, j)
            result.append(count_)
            
result = list(sorted(result))
print(len(result))
print(*result)