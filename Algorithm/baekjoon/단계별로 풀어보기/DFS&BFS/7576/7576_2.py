import sys
from collections import deque

input_ = sys.stdin.readline

def bfs(n, m, matrix, visit):

    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    
    count = -1

    while visit:
        count += 1
        for _ in range(len(visit)):
            x, y = visit.popleft()

            for i in range(4):
                n_x, n_y = x+dx[i], y+dy[i]

                if 0<=n_x<n and 0<=n_y<m:
                    if matrix[n_x][n_y] == 0:
                        matrix[n_x][n_y] = 1
                        visit.append([n_x,n_y])
    
    for search in matrix:
        if 0 in search:
            return -1
    
    return count


if __name__ == "__main__":
    m, n = map(int, input_().split())

    matrix, visit = [], deque()

    for i in range(n):
        row = list(map(int, input_().split()))
        for j in range(m):
            if row[j] == 1:
                visit.append([i,j])
        matrix.append(row)

    answer = bfs(n, m, matrix, visit)
    print(answer)