# 순열 확인. 서로 순열 관계에 있는지 확인하는 메서드를 작성하라.
# 순열 관계라는 단어가 익숙치 않고 정확하게 정의가 안된다.
# 먼저.. 순열 관계라면 문자열의 길이가 같다. 

# 따라서 쉽게 생각해볼때 문자열 두 개를 각각 정렬하여 비교하는 방법을 생각할 수 있다.
# 또한, 알파벳의 개수를 셀 수도 있다.



# 1. 문자열 두개를 각각 정렬하여 비교.
# python 의 정렬 메소드의 시간복잡도는 O(nlogn)이 걸린다. 
def solution(a, b):
    # 문자열의 길이 비교.
    if len(a) != len(b):
        return False
    
    a = sorted(a)
    b = sorted(b)

    if a == b:
        return True
    return False
