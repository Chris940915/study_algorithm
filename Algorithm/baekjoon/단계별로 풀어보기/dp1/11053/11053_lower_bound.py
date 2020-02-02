

def lower_bound(start, end, n_list, k):

    while(end-start > 0):
        m = (start+end)//2 
        if n_list[m] < k:
            start = m + 1
        else:
            end = m
    return end+1

n = int(input())
result = list()

n_list = list(map(int, input().split()))
sorted_list = sorted(n_list)

result.append(n_list[0])

for i in range(1, n):
    if result[-1] < n_list[i]:
        result.append(n_list[i])
    else:
        seq = lower_bound(0, len(result), result, n_list[i])
        result[seq-1] = n_list[i]

print(len(result))
