from itertools import combinations
from collections import deque
import copy

def spread_bfs(graph, a, b):
    queue = [(a,b)]

    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    while queue:
        x, y = queue.pop(0)

        for i in range(4):
            n_x, n_y = x+dx[i], y+dy[i]

            if 0<=n_x<n and 0<=n_y<n:
                if graph[n_x][n_y] == 0:
                    graph[n_x][n_y] = 2 
                    queue.append((n_x, n_y))

# 전체 매트릭스에서 0인 좌표들의 조합을 만들어낸다. 
def generation_zero(matrix):

    zero_ = []

    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 0:
                zero_.append([i,j])
    
    zero_list = list(combinations(zero_, 3))

    return zero_list


if __name__ == "__main__":
    n, m = map(int, input().split())

    matrix = []
    
    for _ in range(n):
        matrix.append(list(map(int, input().split())))
    
    zero_matrix = generation_zero(matrix)
    answer = []

    for n_ in zero_matrix:
        for idx in range(3):
            matrix[n_[idx][0]][n_[idx][1]] = 1

        copy_matrix = copy.deepcopy(matrix)
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 2:
                    spread_bfs(copy_matrix, i, j)
        count = 0
        for i in range(n):
            for j in range(m):
                if copy_matrix[i][j] == 0:
                    count += 1
        answer.append(count)

        for idx in range(3):
            matrix[n_[idx][0]][n_[idx][1]] = 0

    print(max(answer))