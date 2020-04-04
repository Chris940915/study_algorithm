


n = int(input())
m = int(input())

matrix = [[0]*n for _ in range(n)]

for _ in range(m):
    a, b = map(int, input().split())
    matrix[a-1][b-1] = 1

for k in range(n):
    for i in range(n):
        if matrix[i][k] == 0: continue
        for j in range(n):
            if matrix[k][j]:
                matrix[i][j] = 1

count_list = []
for idx in range(n):
    count = 0 
    res = matrix[idx]

    for i in range(n):
        if i == idx:
            continue
        if matrix[i][idx]:
            res[i] = 1
    
    for i, r in enumerate(res):
        if i == idx:
            continue
        if r != 1:
            count += 1
    count_list.append(count)

for c in count_list:
    print(c)
