
def solution(x_, y_, count, graph):
    dx = [0,0,1,-1] 
    dy = [1,-1,0,0]

    graph[x_][y_] = 0
    
    for i in range(4):
        nx, ny = dx[i]+x_, dy[i]+y_

        if 0<= nx < n and 0<= ny < n:
            if matrix[nx][ny]:
                count = solution(nx, ny, count+1, graph)

    return count


if __name__ == "__main__":
    n = int(input())
    matrix = [list(map(int, list(input()))) for _ in range(n)]
    
    result = list()

    for i in range(n):
        for j in range(n):
            if matrix[i][j] == 1:
                result.append(solution(i, j, 1, matrix))

    print(len(result))
    result = sorted(result)
    for i in result:
        print(i)
