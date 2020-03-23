

#   중복이 없는지 판단하는 방법은 해쉬 테이블을 이용하면 쉽게 풀 수 있다.
#   파이썬의 해쉬 테이블은 쉽게 dictionary 자료형을 사용하여 구현할 수 있다.
#   1. 자료구조를 사용한 풀이 (dictionary 사용)
#   
#   또한, 자료구조를 사용하지 않고 풀기 위해선 이중 for문을 돌려서 확인해야한다. 
#   2. 이중 for문을 이용한 풀이. 

# 1. 자료구조를 사용한 풀이.
#  hashtable의 접근 시간복잡도는 O(1)으로 빠르다.
#  따라서 이 풀이의 시간복잡도는 O(n)이며, 다 접근하는게 아니기 때문에 상수라고 주장할 수 있다.
#  공간 복잡도는 O(n) 이다.

def solve_1(text):
    character_dict = dict()

    for t in text:
        if t in character_dict:
            return False
        else:
            character_dict[t] = 1
    return True


# 2. 이중 for 문을 이용한 풀이.
# 이렇게 풀게되면 for문을 2개 사용하여 시간복잡도가 O(n^2)이 된다. 

def solve_2(text):
    n = len(text)

    for i in range(n-1):
        for j in range(i+1, n):
            if text[i] == text[j]:
                return False
    return True

# solution
# 먼저 면접관에게 문자열이 아스키 코드인지 유니코드인지 물어봐야 한다.
# 따른 문제를 푸는 방법은 문자 집합에서 i번째 문자열이 존재하는지를 boolean 배열로 나타내는 것이다.  



