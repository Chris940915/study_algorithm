from collections import deque

def bfs(start, up, down, height, goal):
    queue = deque([start])
    visit[start] = 1

    while queue:
        x = queue.popleft()

        for nx in [x+up, x-down]:
            if 1<=nx and nx<=height:
                if visit[nx] == 0:
                    visit[nx] = visit[x]+1
                    queue.append(nx)

    if visit[goal] == 0:
        print("use the stairs")
    else:
        print(visit[goal]-1)

f, s, g, u, d = map(int, input().split())
visit = [0]*(f+1)

bfs(s, u, d, f, g)
