import sys

sys.setrecursionlimit(20000)

def dfs(x):
    global result

    visited[x] = True
    cycle.append(x)
    number = path[x]-1

    if visited[number]:
        if number in cycle:
            result += cycle[cycle.index(number):]
        return
    else:
        dfs(number)


t = int(input())

for _ in range(t):
    n = int(input())
    path = list(map(int, input().split()))
    visited = [False] * n
    result = []
    for idx in range(n):
        if not visited[idx]:
            cycle = []
            dfs(idx)
    print(n-len(result))

