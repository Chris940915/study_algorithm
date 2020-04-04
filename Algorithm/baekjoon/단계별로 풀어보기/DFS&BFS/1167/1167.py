
from collections import deque

def bfs(s, mode):
    q = deque()
    q.append(s)
    visit = [-1]*v
    visit[s] = 0

    while q:
        x = q.popleft()

        for nx, value in matrix[x]:
            if visit[nx] == -1:
                visit[nx] = visit[x] + value
                q.append(nx)
    
    if mode == 1:
        return visit.index(max(visit))
    else:
        return max(visit)



v = int(input())
matrix = [[] for _ in range(v)]

for _ in range(v):
    numbers = list(map(int, input().split()))
    number = numbers[0]

    numbers = numbers[1:-1]
    for i in range(0, len(numbers), 2):
        matrix[number-1].append([numbers[i]-1, numbers[i+1]])

print(bfs(bfs(0, 1), 0))