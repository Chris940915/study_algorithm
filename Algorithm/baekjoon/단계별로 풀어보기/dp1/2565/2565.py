def solution_(n_list):

    len_ = len(n_list)

    # 왼쪽 전봇대를 기준으로 정렬. 
    sorted_list = sorted(n_list, key=lambda x: x[0])
    result = [1 for _ in range(len_)]

    for i in range(1, len_):
        for j in range(i):
            # 이 부분에서 오른쪽 전봇대들을 비교하는 것 주의.
            if sorted_list[i][1] > sorted_list[j][1]:
                if result[i] <= result[j]:
                    result[i] = result[j]+1

    return result


if __name__ == "__main__":
    n = int(input())
    n_list = list()

    for i in range(n):
        n_list.append(list(map(int, input().split())))

    solution = solution_(n_list)
    print(n-max(solution))
