
def check(dist):
    count = 1
    stand = homes[0]

    for i in range(1, n):
        if stand+dist <= homes[i]:
            count += 1
            stand = homes[i]
    return count


def binary_search(lower, upper, target):

    while lower <= upper:
        mid = (lower+upper)//2

        if check(mid) >= target:
            lower = mid + 1
        elif check(mid) < target:
            upper = mid - 1
    return upper



n, c = map(int, input().split())

homes = []
for _ in range(n):
    homes.append(int(input()))

homes = sorted(homes)
low, up = 1, homes[-1]-homes[0]

res = binary_search(low, up, c)
print(res)

