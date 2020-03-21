import sys
from itertools import combinations

input_ = sys.stdin.readline


def calculation(matrix, x, y):
    return matrix[x-1][y-1]+matrix[y-1][x-1]

def solution(n, matrix):

    members = [i+1 for i in range(n)]
    mid = n//2

    teams = combinations(members, mid)
    # set의 '-' 연산을 하기 위하여.
    members = set(members)

    min_V = sys.maxsize

    for team in teams:
        start = set(list(team))
        link = members-start

        starts_combination = combinations(start, 2)
        start_sum = 0
        for starts in starts_combination:
            start_sum += calculation(matrix, starts[0], starts[1])
            #calculation(matrix, starts[0], starts[1])

        link_sum = 0
        links_combination = combinations(link, 2)
        for links in links_combination:
            link_sum += calculation(matrix, links[0], links[1])

        min_V = min(abs(start_sum-link_sum), min_V)
    print(min_V)


if __name__ == "__main__":
    
    n = int(input_())
    matrix = [list(map(int, input_().split())) for _ in range(n)]

    solution(n, matrix)



