#
#   s1 과 s2 두 문자열이 포함되는지.
#
#  아주 쉬운 문제이지만 아이디어를 생각하는 것이 중요하다. 

def solve(s1, s2):
    s1s1 = s1+s1

    answer = isSubstring(s1s1, s2)
    
    print(answer)