import  sys
from bisect import bisect_left



n = int(sys.stdin.readline())
numbers = list(map(int, sys.stdin.readline()))
stack = [0]

for i in range(n):
    if stack[-1] < numbers[i]:
        stack.append(numbers[i])
    else:
        stack[bisect_left(stack, numbers[i])] = numbers[i]
print(len(stack)-1)