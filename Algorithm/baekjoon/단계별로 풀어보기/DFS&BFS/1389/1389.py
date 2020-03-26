from collections import deque
import sys

def bfs(a):
    queue = deque([a])

    visit = [0]*n
    visit[a] = 1

    while queue:
        x = queue.popleft()

        for idx in range(n):
            if matirx[x][idx] and not visit[idx]:
                visit[idx] = visit[x]+1
                queue.append(idx)
    sum_ = sum(visit) - n
    return sum_



n, m = map(int, input().split())
matirx = [[0]*n for _ in range(n)]

for _ in range(m):
    a, b = map(int, input().split())
    matirx[a-1][b-1] = 1
    matirx[b-1][a-1] = 1

min_V = sys.maxsize

answer = 0

for i in range(n):
    if min_V > bfs(i):
        min_V = bfs(i)
        answer = i
print(answer+1)
