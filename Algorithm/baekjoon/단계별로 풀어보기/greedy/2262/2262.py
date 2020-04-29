

n = int(input())
numbers = list(map(int, input().split()))

tot = 0

while True:
    max_V = max(numbers)
    idx = numbers.index(max_V)
    n_n = len(numbers)

    if n_n == 1:
        print(tot)
        break

    if idx == 0: 
        diff = numbers[idx] - numbers[idx+1]

    elif idx == n_n-1:
        diff = numbers[idx] - numbers[idx-1]
        
    else:
        if numbers[idx-1] < numbers[idx+1]:
            diff = numbers[idx] - numbers[idx+1]
        else:
            diff = numbers[idx] - numbers[idx-1]
    tot += diff
    numbers.pop(idx)

