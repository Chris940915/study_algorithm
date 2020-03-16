import copy

def solution(a, b, graph):
    # 방문한 점은 0으로 초기화하여 다시 안들리게.
    graph[a][b] = 0
    visit = [(a,b)]
    queue = [(a,b)]
    count = 1

    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    while queue:
        x, y = queue.pop(0)

        for i in range(4):
            new_x, new_y = dx[i]+x, dy[i]+y

            if 0<=new_x<n and 0<=new_y<n:
                if not (new_x, new_y) in visit and graph[new_x][new_y]:
                    queue.append((new_x, new_y))
                    graph[new_x][new_y] = 0
                    count += 1
    return count



if __name__ == "__main__":
    
    n = int(input())

    matrix = []
    for _ in range(n):
        matrix.append(list(map(int, list(input()))))

    visit = matrix.copy()

    result = []

    for i in range(n):
        for j in range(n):
            if matrix[i][j] == 1:
                result.append(solution(i,j, matrix))
    
    print(len(result))
    result = sorted(result)
    for i in result:
        print(i)