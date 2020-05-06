

n = int(input())
tower = list(map(int, input().split()))
stack = []
res = [0] * n

# 1번 풀이
# 뒤에서부터 보고 온다.
'''
for i in range(n-1, -1, -1):
    while stack and tower[stack[-1]] < tower[i]:
        temp = stack.pop()
        res[temp] = i+1
    stack.append(i)
print(*res)
'''


# 2번 풀이
# 앞에서부터 보고 작으면 버린다. 
for i in range(n):
    while stack and tower[stack[-1]] < tower[i]:
        stack.pop()
    if stack:
        res[i] = stack[-1]+1
    stack.append(i)
print(*res)