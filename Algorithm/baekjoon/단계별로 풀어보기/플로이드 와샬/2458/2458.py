
n, m = map(int, input().split())
matrix = [[0]*n for _ in range(n)]

for _ in range(m):
    a, b = map(int, input().split())

    matrix[a-1][b-1] = 1

for k in range(n):
    for i in range(n):
        if matrix[i][k] == 0: continue
        for j in range(n):
            if matrix[i][k] and matrix[k][j]:
                matrix[i][j] = 1

count = 0
for idx in range(n):
    res = []
    res = matrix[idx]

    for i in range(n):
        if i == idx:
            continue
        if matrix[i][idx] == 1:
            res[i] = 1
    
    flag = False
    for i, r in enumerate(res):
        if idx == i:
            continue
        
        if r != 1:
            flag = True
            break
        flag = False
    if not flag:
        count += 1
print(count)
