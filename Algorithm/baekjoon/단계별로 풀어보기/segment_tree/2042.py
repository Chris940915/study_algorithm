
def init(n, start, end):
    if start==end:
        tree[n] = l[start]
        return tree[n]
    else:
        tree[n] = init(n*2, start, (start+end)//2) + init(n*2+1, (start+end)//2+1, end)
        return tree[n]

def subSum(n, start, end, left, right):
    
    if start > right or end < left:
        return 0

    if left <= start and end <= right:
        return tree[n]

    return subSum(n*2, start, (start+end)//2, left, right) + subSum(n*2+1, (start+end)//2+1, end, left, right)


def update(n, start, end, index, diff):
    if index < start or end < index:
        return
    
    tree[n] += diff

    if start != end:
        update(n*2, start, (start+end)//2, index, diff)
        update(n*2+1, (start+end)//2+1, end, index, diff)



n, m, k = map(int, input().split())
l = []
tree = [0]*3000000

for _ in range(n):
    l.append(int(input()))

init(1, 0, n-1)

for _ in range(m+k):
    a, b, c = map(int, input().split())

    if a == 1:
        b = b-1
        diff = c-l[b]
        l[b] = c
        update(1, 0, n-1, b, diff)
    else:
        print(subSum(1, 0, n-1, b-1, c-1))
