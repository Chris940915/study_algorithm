

def lower_bound(start, end, n_list, k):

    while(end-start > 0):
        m = (start+end)//2 
        if n_list[m] < k:
            start = m + 1
        else:
            end = m
    return end+1

def solution_(n, n_list):
    result = list()
    result.append(n_list[0])

    for i in range(1, n):
        if result[-1] < n_list[i]:
            result.append(n_list[i])
        else:
            seq = lower_bound(0, len(result), result, n_list[i])
            result[seq-1] = n_list[i]

    print(len(result))

n = int(input())

n_list = list(map(int, input().split()))

solution_(n, n_list)


