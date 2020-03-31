from collections import deque
import sys

input_ = sys.stdin.readline


def cal_distance(coordi, places):
    distances = []
    for p in places:
        distances.append(abs(coordi[0]-p[0])+abs(coordi[1]-p[1]))
        
    return distances


def bfs(n):
    visited = [-1]*(n+2)
    visited[0] = 0 

    queue = deque()
    queue.append(places[0])
    
    while queue:
        q = queue.popleft()
        distances = cal_distance(q, places)
        for i, d in enumerate(distances):
            if visited[i] == -1 and d > 0 and d <= 1000:
                queue.append(places[i])
                visited[i] = 0
    if visited[-1] == -1:
        print('sad')
    else:
        print('happy')


    
T = int(input_())

for _ in range(T):
    n = int(input_())

    #start = list(map(int, input_().split()))
    places = []
    for i in range(n+2):
        places.append(list(map(int, input_().split())))
    #goal = list(map(int, input_().split()))
    bfs(n)
