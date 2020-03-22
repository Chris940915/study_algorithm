
def solution(a, b):
    n = len(b)
    result = []
    pointer = 0

    while pointer < len(a):
        result.append(a[pointer])
        pointer += 1

        flag = True

        if len(result) >= n:
            for i in range(-1, -n-1, -1):
                if result[i] != b[i]:
                    flag = False
                    break
            
            if flag:
                for _ in range(n):
                    result.pop()
    return result



if __name__ == "__main__":
    
    text_1 = input()
    text_2 = input()

    answer = solution(text_1, text_2)

    if answer:
        print(''.join(answer))
    else:
        print("FRULA")