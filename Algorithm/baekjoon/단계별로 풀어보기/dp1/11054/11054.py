

# 일반적인 LIS와 동일. 
def solution_(n_list):

    len_ = len(n_list)
    result = [1 for _ in range(len_)]

    for i in range(1, len_):
        for j in range(i):
            # 입력한 숫자 i 보다 i 이전의 숫자들 j 가 작고,
            if n_list[i] > n_list[j]:
                # 숫자 i 까지 순열의 길이보다 j 까지 순열의 길이가 같거나 크면, 
                if result[i] <= result[j]:
                    result[i] = result[j] + 1
    return result



if __name__ == "__main__":
    n = int(input())
    n_list = list(map(int, input().split()))
    reversed_list = list(reversed(n_list))

    first_ = solution_(n_list)
    # 결과값도 뒤집어준다. 
    second_ = list(reversed(solution_(reversed_list)))

    solution = list()

    for a, b in zip(first_, second_):
        solution.append(a+b)

    # 중간값이 겹치기 떄문에 -1 해준다. 
    print(max(solution)-1)