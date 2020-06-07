from collections import deque

q = deque()

n = int(input())
path = [[] for _ in range(n)]
time = [0]*n
indegree = [0]*n
result = [0]*n

for i in range(n):
    enter = list(map(int, input().split()))
    time[i] = enter[0]
    if len(enter) == 2:
        result[i] = enter[0]
        q.append(i)
        continue
    
    enter = enter[1:-1]

    for e in enter:
        path[e-1].append(i)
        indegree[i] += 1

while q:
    x = q.popleft()

    for search in path[x]:
        result[search] = max(result[search], result[x]+time[search])
        indegree[search] -= 1
        
        if indegree[search] == 0:
            q.append(search)
for i in result:
    print(i)