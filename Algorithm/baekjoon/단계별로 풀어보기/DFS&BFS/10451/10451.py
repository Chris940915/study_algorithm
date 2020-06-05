import sys

sys.setrecursionlimit(2000)

t = int(input())

def dfs(x, path, visit):
    if visit[x]:
        return
    visit[x] = 1
    dfs(path[x]-1, path, visit)

for _ in range(t):
    n = int(input())
    path = list(map(int, input().split()))
    visit = [False]*n
    count = 0
    for idx in range(n):
        if not visit[idx]:
            dfs(idx, path, visit)
            count += 1
    print(count)
