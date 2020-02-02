

def solution_(n):
    result = [1 for _ in range(n)] 

    for i in range(n):
        for j in range(i):
            if n_list[i] > n_list[j]:
                if result[i] <= result[j]:
                    result[i] = result[j] + 1
    return max(result)


n = int(input())

n_list = list(map(int, input().split()))

solution = solution_(n)
print(solution)


