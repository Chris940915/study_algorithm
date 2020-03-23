# 하나 빼기
# 문자열 두개를 같게 하기위한 편집 횟수가 1회 이내인지 확인하는 함수. 
# 문자 삽입, 문자 삭제는 문자열 길이가 다를때 일어나는 것. 
# 문자 교체는 문자열의 길이가 같을때 일어나는 것. 케이스 분류를 한다. 


def solve(a, b):

    # 문자열의 길이가 같아 문자 교체.
    # 문자 교체를 할때는 다른 문자열이 1개 이하면 편집 횟수가 1회 이내가 된다.
    length = len(a)-len(b)
    if length == 0:
        count = 0 
        # 문자 각각을 비교.
        for i, j in zip(a, b):
            if i != j:
                count += 1

        # 두개이상 다를때 False 리턴.
        if count > 1:
            return False
        else:
            return True
    
    #문자열의 길이가 다를때는 문자 삽입 또는 문자 삭제.
    # a를 기준으로하면, a가 더 길기 때문에 a에서 문자 삭제를 한다.
    elif length > 0:
        idx = -1
        for i in range(len(b)):
            if a[i] != b[i]:
                idx = i
                break
        
        if idx == -1:
            a.pop()
        else:
            a.pop(idx)
        
        if a == b:
            return True
        else:
            return False

    # a를 기준으로하면, a가 더 짧기 때문에 a에 문자 삽입을 한다.
    elif length < 0:
        idx = -1
        for i in range(len(b)):
            if a[i] != b[i]:
                idx = i
                break
        
        if idx == -1:
            a += b[-1]
        else:
            a = a[:idx]+b[idx]+a[idx:]
        
        if a == b:
            return True
        else:
            return False
