
from collections import deque

n, m = map(int, input().split())
path = [[] for _ in range(n)]
visited = [False] * n
q = deque()
indegree = [0] * n
result = []

for i in range(m):
    enter = list(map(int, input().split()))
    enter_n = enter[0]
    enter = enter[1:]

    for idx in range(enter_n-1):
        path[enter[idx]-1].append(enter[idx+1]-1)
        indegree[enter[idx+1]-1] += 1

for i in range(n):
    if indegree[i] == 0:
        q.append(i)

while q:
    x = q.popleft()
    result.append(x)
    for search in path[x]:
        indegree[search] -= 1
        
        if indegree[search] == 0:
            q.append(search)

if len(result) != n:
    print(0)
else:
    for i in result:
        print(i+1)

