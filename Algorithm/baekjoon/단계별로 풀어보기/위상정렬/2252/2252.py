from collections import deque

n, m = map(int, input().split())
matrix = [[] for _ in range(n)]
indegree = [0]*n
result = []
q = deque()

for _ in range(m):
    a, b = map(int, input().split())
    matrix[a-1].append(b-1)
    indegree[b-1] += 1

for i in range(n):
    if indegree[i] == 0:
        q.append(i)

while q:
    x = q.popleft()
    result.append(x)

    for search in matrix[x]:
        indegree[search] -= 1
    
        if indegree[search] == 0:
            q.append(search)

for r in result:
    print(r+1, end=' ')