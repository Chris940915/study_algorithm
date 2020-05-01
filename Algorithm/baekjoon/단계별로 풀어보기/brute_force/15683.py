

def watch(x, y, directions):
    coor_set = set()

    for d in directions:
        nx, ny = x, y
        while 1:
            nx, ny = dx[d]+nx, dy[d]+ny
            if 0<=nx<n and 0<=ny<m:
                if matrix[nx][ny] == 6:
                    break

                if matrix[nx][ny] == 0:
                    coor_set.add((nx, ny))
            else:
                break
    return coor_set


def dfs(cnt, union_set):
    global max_v

    if cnt == len(all_cctv):
        max_v = max(max_v, len(union_set))
        return 

    else:
        for i in all_cctv[cnt]:
            dfs(cnt+1, union_set|i)
    


n, m = map(int, input().split())

matrix = [list(map(int, input().split())) for _ in range(n)]
empty = 0

# 위, 오른쪽, 아래, 왼쪽
dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]

all_cctv = []
max_v = 0

for i in range(n):
    for j in range(m):
        if matrix[i][j] == 0: empty += 1

        elif matrix[i][j] == 1: 
            all_cctv.append([watch(i, j, [0]), watch(i, j, [1]), watch(i, j, [2]), watch(i, j, [3])])
        
        elif matrix[i][j] == 2:
            all_cctv.append([watch(i, j, [0,2]), watch(i, j, [1,3])])
        
        elif matrix[i][j] == 3:
            all_cctv.append([watch(i, j, [0,1]), watch(i, j, [1,2]), watch(i, j, [2,3]), watch(i, j, [3,0])])

        elif matrix[i][j] == 4:
            all_cctv.append([watch(i, j, [0,1,2]), watch(i, j, [1,2,3]), watch(i, j, [2,3,0]), watch(i, j, [3,0,1])])

        elif matrix[i][j] == 5:
            all_cctv.append([watch(i, j, [0,1,2,3])])
 
dfs(0, set())
print(empty-max_v)