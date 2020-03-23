# 행렬 M X N 의 한 원소가 0 일 경우, 해당 원소가 속한 열과 행 모드를 0으로 설정.
#
#  0의 특정 위치를 생각하여 이차원 배열에 위치를 담을 수도 있다.
#  하지만, 1차원 배열에 위치를 담는다면, 공간 복잡도가 O(n)이 된다.
#

# 특정 위치 기록시 공간 복잡도 O(MN)
def slove(matrix, n, m):
    zeros = []

    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 0:
                zeros.append([i,j])
    
    for zero in zeros:
        for x in range(m):
            matrix[x][zeros[1]] = 0
        
        for y in range(n):
            matrix[zeros[0][y]] = 0
    
    return zeros

# boolean으로 각 열과 행을 기록시 O(n)으로 공간복잡도를 줄일 수 있다. 
def solution(matrix, n, m):
    rows = [False] * m
    cols = [False] * n

    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 0:
                rows[i] = True
                cols[j] = True
    
    for i in range(m):
        if rows[i]:
            for j in range(n):
                matrix[i][j] = 0

    for i in range(n):
        if cols[i]:
            for j in range(m):
                matrix[j][i] = 0

    return matrix