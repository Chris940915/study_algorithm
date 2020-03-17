import copy

def spread(_virus_l, c_arr):
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    virus_count = 0
    global safe_area

    while _virus_l:
        x, y = _virus_l.pop()
        for i in range(4):
            n_x, n_y = x+dx[i], y+dy[i]

            if 0<=n_x<n and 0<=n_y<m:
                if c_arr[n_x][n_y] == 0:
                    c_arr[n_x][n_y] = 2
                    virus_count += 1
                    _virus_l.add((n_x, n_y))
    
    return safe_area - virus_count - 3


def generation_wall(start, no_wall):
    global maxVal
    global n 
    global m

    if no_wall == 0:
        copy_arr = copy.deepcopy(arr)
        copy_virus = copy.deepcopy(virus_l)

        sCount = spread(copy_virus, copy_arr)
        maxVal = max(sCount, maxVal)
        return
    
    for i in range(start, n*m):
        x = i // m
        y = i % m

        if arr[x][y] == 0:
            arr[x][y] = 1
            generation_wall(i+1, no_wall-1)
            arr[x][y] = 0

if __name__ == "__main__":
    
    n, m = map(int, input().split())

    virus_l = set()
    arr = []
    maxVal = 0
    safe_area = 0

    for _ in range(n):
        arr.append(list(map(int, input().split())))
    
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 2:
                virus_l.add((i,j))
            elif arr[i][j] == 0:
                safe_area += 1
    generation_wall(0, 3)
    print(maxVal)