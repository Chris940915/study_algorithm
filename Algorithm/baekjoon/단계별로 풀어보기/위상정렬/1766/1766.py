
import heapq

n, m = map(int, input().split())
path = [[] for _ in range(n)]
indegree = [0]*n
heap = []
result = []

for _ in range(n):
    a, b = map(int, input().split())
    path[a-1].append(b-1)
    indegree[b-1] += 1

for i in range(n):
    if indegree[i] == 0:
        heapq.heappush(heap, i)

while heap:
    x = heapq.heappop(heap)
    result.append(x)

    for search in path[x]:
        indegree[search] -= 1

        if indegree[search] == 0:
            heapq.heappush(heap, search)

for i in result:
    print(i+1, end=' ')

