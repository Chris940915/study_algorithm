def solution_(n, k):
    result = [[0 for _ in range(k+1)] for _ in range(n+1)]

    w_list = [0]
    v_list = [0]

    for i in range(n):
        w, v = map(int, input().split())
        w_list.append(w)
        v_list.append(v)
    
    for i in range(1, n+1):
        for j in range(1, k+1):
            if j < w_list[i]:
                result[i][j] = result[i-1][j]
            else:
                result[i][j] = max(result[i-1][j], result[i-1][j-w_list[i]]+v_list[i])
    return result[n][k]



if __name__ == "__main__":
    n, k = map(int, input().split())

    solution = solution_(n, k)
    print(solution)

