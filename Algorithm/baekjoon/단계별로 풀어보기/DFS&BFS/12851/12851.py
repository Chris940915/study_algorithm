
import sys
from collections import deque

LIMIT = 100001
input_ = sys.stdin.readline

def bfs(n, k, visit, way):
    queue = deque([n])

    # 길로 가는 최단거리
    visit[n] = 0
    # 최단거리로 가는 경우의 수 
    way[n] = 1

    while queue:
        x = queue.popleft()

        for n_x in (x-1, x+1, x*2):
            if 0<=n_x<LIMIT:
                if visit[n_x] == LIMIT:
                    visit[n_x] = visit[x]+1
                    way[n_x] = way[x]
                    queue.append(n_x)
                elif visit[n_x] == visit[x]+1:
                    way[n_x] += way[x]
    print(visit[k])
    print(way[k])



if __name__ == "__main__":
    n, k = map(int, input_().split())

    ## 가지수에 LIMIT 값을 집어넣어야 반례에 걸리지 않는다. 

    visit = [LIMIT]*LIMIT
    way = [0]*LIMIT

    bfs(n, k, visit, way)
