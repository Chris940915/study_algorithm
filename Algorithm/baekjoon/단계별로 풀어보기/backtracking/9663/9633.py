
#  들어오는 값이 n 보다 크거나 같을때 종료.
#  
#

def check(x, cols):
    for i in range(x):
        if cols[i] == cols[x] or abs(cols[i]-cols[x]) == x-i:
            return False
    return True

def solution(x, cols):
    global count

    if x == n:
        count += 1
        return
    
    else:
        for i in range(n):
            cols[x] = i
            if check(x, cols):
                solution(x+1, cols)

if __name__ == "__main__": 
    n = int(input())
    cols = [0]*n
    count = 0
    solution(0, cols)

    print(count)