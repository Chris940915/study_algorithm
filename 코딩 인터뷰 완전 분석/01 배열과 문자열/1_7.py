

def rotate_90(m):
    N = len(m)

    ret = [[0]*N for _ in range(N)]

    for row in range(N):
        for col in range(N):
            ret[col][N-1-row] = m[row][col]
    return ret

def rotate_180(m):
    N = len(m)
    ret = [[0]*N for _ in range(N)]

    for row in range(N):
        for col in range(N):
            ret[N-1-row][N-1-col] = m[row][col]
    return ret

def rotate_270(m):
    N = len(m)
    ret = [[0]*N for _ in range(N)]

    for row in range(N):
        for col in range(N):
            ret[N-1-col][row] = m[row][col]
    return ret