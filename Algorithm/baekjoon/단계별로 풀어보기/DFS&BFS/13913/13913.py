from collections import deque
import sys

input_ = sys.stdin.readline
LIMIT = 100001

def bfs(n, k):
    queue = deque([n])
    visit[n] = 0
    path[n] = 0
    T = []

    if n == k:
        return 0, [k]

    while queue:
        x = queue.popleft()

        if x == k:
            temp = x
            # 최단 경로의 개수만큼 길을 리스트에 담는다.
            for _ in range(visit[x]):
                T.append(path[temp])
                temp = path[temp]
            T = list(reversed(T))
            # 해당 값을 리스트에 담는다. 
            T.append(k)
            return visit[x], T

        for n_x in (x-1, x+1, x*2):
            if 0<=n_x<LIMIT:
                if visit[n_x] == LIMIT:
                    queue.append(n_x)
                    path[n_x] = x
                    visit[n_x] = visit[x] + 1
 
n, k = map(int, input_().split())

#최단경로.
visit = [LIMIT]*LIMIT
# 돌아가는 길을 담는 리스트. 
path = [LIMIT]*LIMIT

answer, numbers = bfs(n, k)

print(answer)
print(*numbers)