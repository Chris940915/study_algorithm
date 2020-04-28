import sys
import copy

MAX = sys.maxsize


def check(list_, i, tall_no, j):
    copy_ans = copy.deepcopy(list_)

    copy_ans[j] = i+1
    count = 0

    for idx in range(j):
        if copy_ans[idx] > copy_ans[j]:
            count += 1
    
    if count != seq[i]:
        return False
    else:
        return True

n = int(input())

seq = list(map(int, input().split()))
answer = [MAX] * n

answer[seq[0]] = 1

for i in range(1, n):

    for j in range(n):
        if answer[j] == MAX:
            if check(answer, i, seq[i], j):
                answer[j] = i+1
                break
print(*answer)

