

'''
    N 과 M 문제를 그렇게 풀어제꼈는데 못풀다니..

    나는 바보멍충이다.
'''

k = int(input())
operators = input().split()
max_v, min_v = '', ''
check_list = [False]*10

def solve(cnt, s):
    global max_v, min_v

    if cnt == k+1:
        if not min_v:
            min_v = s
        else:
            max_v = s
        return

    for idx in range(10):
        if not check_list[idx]:
            if cnt == 0 or check(int(s[-1]), idx, operators[cnt-1]):
                check_list[idx] = True
                solve(cnt+1, s+str(idx))
                check_list[idx] = False


def check(i, j, k):

    if k == '>':
        return i > j
    else:
        return i < j


solve(0, '')
print(max_v)
print(min_v)
