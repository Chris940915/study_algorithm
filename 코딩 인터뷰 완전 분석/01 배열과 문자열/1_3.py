# URL 화.
# 아주 쉬운 문제다. 문자열에 들어 있는 모든 공백을 바꾸라니.
# python은 문자열을 배열로 봐서 쉽게 풀 수 있다.

def solve(text):
    result = ''

    for t in text:
        if t == ' ':
            result += '%20'
        else:
            result += t
    return result
