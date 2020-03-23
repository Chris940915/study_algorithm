# 문자열 압축
# 문자의 개수를 세는 방식의 기본적인 문자열 압축 메서드를 작성하라.
# 
# for 문으로 돌면서 앞과 뒤가 문자가 다르면 count한 개수를 문자열에 붙이는 방식으로 풀이.
# 


def solve(text):
    n = len(text)
    result = ''
    count = 1
    for i in range(n):
        # 
        if i == (n-1) or text[i] != text[i+1] :
            result += text[i]+str(count)
            count = 1
        else:
            count += 1
    print(result)

solve('aabccccaaa')