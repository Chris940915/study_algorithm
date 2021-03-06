
# Dynamic Programming
  
  Mermorization(Top-down) vs Dynamic Programming(Botton-up)         
* 순환식의 값을 계산하는 기법들.          
* 둘 다 동적계획법의 일종.        
* top-down은 실제로 필요한 subproblem만을 푼다.        
* bottom-up은 recusion에 수반되는 overhead가 없다.   
    
가장 대표적인건 피보나치 수열.

<pre>
  <code>
    def fib(n):
      if n==1 or n==2:
        return 1
      else:
        return fib(n-1) + fib(n-2)
  </code>
</pre>

많은 계산이 중복된다.    
계산을 버리지 않고 기억.    
    
**Memoization**
<pre>
  <code>
    def fib(n):
      if n==1 or n==2:
        return 1
      elif f[n]>-1: # 배열 f가 -1으로 초기회되어있다고 가정.
        return f[n]
      else:
        f[n] = fib(n-2) + fib(n-1) # 중간 계산 결과를 caching.
        return f[n]
      
  </code>
</pre>
     
     
**bottom-up 방식**
<pre>
  <code>
    def fib(n):
      f[1], f[2] = 1, 1
      for i in range(3, n+1):
        f[i] = f[i-1]+f[i-2]
      return f[n]
  </code>
</pre>
      
또 다른 예로 이항계수 (Binomial Coefficient - nCk)가 있음.        
n개 중 k를 선택.     

**Memoization**    
<pre>
    <code>
        def binomial(n, k):
            if n==k or k==0:
                return 1
            elif binom[n][k] > -1):
                return binom[n][k]
            else:
                binom[n][k] = binomial(n-1, k) + binomial(n-1, k-1)
                return binom[n][k]
    </code>
</pre>
        
**bottom-up**    
이차원 배열이다보니 bottom-up의 의미는 기본적인 값에서부터 원하는 값으로 올라온다 (그림으로 그려보면 쉽게 이해된다).      
위의 피보나치와 다름.        
<pre>
    <code>
        def binomial(n, k):
            for i in range(n):
                for j in range(i+1):
                    if k == 0 or n == k:
                        binom[i][j] = 1
                    else:
                        binom[i][j] = binom[i-1][j-1] + binom[i-1][j]
            return binom[n][k]
    </code>
</pre>        
위의 예제들은 순환식이 주어지고, 동적 계획법 기법을 적용하라는 문제.     
**하지만 보통의 동적 계획법 문제들은 순환식을 직접 세우고 동적 계획법까지 직접 적용해야한다.**      
동적 계획법 적용은 익숙해지면 쉽기 때문에 순환식을 어떻게 세울거냐의 싸움.      
        
1. 일반적으로 최적화문제(optimisation problem) 혹은 카운팅(counting) 문제에 적용.    
2. 주어진 문제에 대해 순환식(recurrence equation)을 정의한다.    
3. 순환식을 memorization 혹은 bottom-up 방식으로 푼다.    
    
* subproblem 들을 풀어서 문제를 푸는 방식으로 분할정복과 공통점이 있음.    
* 분할정복법의 문제들은 서로 dijoint하지만 동적 계획법은 그렇지않음.    
* **즉 서로 overlapping하는 subproblem들을 해결함으로써 원래 문제를 해결.**  
    
분할정복은 quick sort를 생각하면 된당.    
pivot를 기준으로 분할된 두 subproblem들을 푼다.    
하지만, 행렬경로문제를 생각하면 subproblem들이 겹치는 것은 Dynamic programming이다.    

* Optimal Substructure를 확인하는 질문.    
순환식은 optimal substructure를 표현한다.    
    
**최적해의 일부분이 그 부분에 대한 최적해인가?**    
Yes면 맞지만... 예외.   
최장경로문제가 예외로 있음.   
하지만, subproblem으로 풀 수 있기때문에 다른 형태의 optimal substructure를 가지는 것일 뿐 optimal substructrue를 가지지 않는건 아니다.    




