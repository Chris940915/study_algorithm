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

n = int(input())
path = []

for _ in range(n):
    path.append(int(input()))
visited = [False]*n
result = []
for idx in range(n):
    if not visited[idx]:
        cycle = []
        dfs(idx)
print(len(result))
result = sorted(result)
for i in result:
    print(i+1)