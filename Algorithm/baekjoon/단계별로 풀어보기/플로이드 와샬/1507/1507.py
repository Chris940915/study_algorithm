
'''

    입력으로 플로이드가 계산된 2차원 배열을 준다.
    이 말은 즉, 모든 정점에서 모든 정점까지 최단거리가 계산되어있다 라는 뜻이다.

    그렇다면 도로 개수가 최소가 되게 간선들을 남기려면 어떻게 해야할까?
    이 말도 해석해보자면 그냥 간선의 개수를 구하라는 뜻이다.

'''


def solution():

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if k==i or k==j or i==j:
                    continue
                if matrix[i][j] == matrix[i][k] + matrix[k][j]:
                    answer[i][j] = 0

                if matrix[i][j] > matrix[i][k] + matrix[k][j]:
                    return -1

    sum_ = 0

    for i in range(n):
        for j in range(i, n):
            if answer[i][j]:
                sum_ += matrix[i][j]
    return sum_


n = int(input())
matrix = []
answer = [[1]*n for _ in range(n)]

for _ in range(n):
    enter = list(map(int, input().split()))
    matrix.append(enter)

print(solution())



