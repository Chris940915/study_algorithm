import copy
from collections import deque
import sys


# 모두 익었는지 체크

def check_all(n, m, graph):
    for i in range(m):
        for j in range(n):
            if graph[i][j] == 0:
                return False
    return True

# 먼저, 0을 찾고 근접에 -1만 있는지 check하고 그렇다면 -1 리턴 함수.
def check_cir(n, m, graph):
    for i in range(m):
        for j in range(n):
            if graph[i][j] == 0:
                for idx in range(4):
                    n_x, n_y = i+dx[idx], j+dy[idx]
                    if 0<=n_x<m and 0<=n_y<n:
                        if not graph[n_x][n_y]:
                            return True 
                return False


def bfs(a, b, graph):
    queue = deque([(a,b)])
    visit[a][b] = 1

    while queue:
        x, y = queue.popleft()

        for idx in range(4):
            n_x, n_y = x+dx[idx], y+dy[idx]
            
            if 0<=n_x<m and 0<=n_y<n:
                if graph[n_x][n_y] == 0:
                    graph[n_x][n_y] = 1
                    
                    if visit[n_x][n_y] == 0:
                        #이 아이디어를 생각못해서 overlap 되게 짰다.  
                        visit[n_x][n_y] = visit[x][y]+1
                    else:
                        visit[n_x][n_y] = min(visit[x][y]+1, visit[n_x][n_y])
                    queue.append((n_x, n_y))

n, m = map(int, sys.stdin.readline().split())
matrix = [(list(map(int, sys.stdin.readline().split()))) for _ in range(m)]

# visit 배열에 몇번째에 지나가는지를 저장.
visit = [[0]*n for _ in range(m)]

dx = [0,0,1,-1]
dy = [1,-1,0,0]
count = 1
max_V = 0

if check_all(n, m, matrix):
    print(0)

elif check_cir(n, m, matrix):
    # 토마토 익는 함수. 
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 1:
                copy_matrix = copy.deepcopy(matrix)
                bfs(i, j,copy_matrix)
    
    for search in visit:
        max_V = max(max(search), max_V)
    print(max_V-1)
else:
    print(-1)