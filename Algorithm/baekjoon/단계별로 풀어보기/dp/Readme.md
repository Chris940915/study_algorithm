
# Dynamic Programming
    
    
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
    
**Memorization**
<pre>
  <code>
    def fib(n):
      if n==1 or n==2:
        return 1
      elif f[n]>-1: # 배열 f가 -1으로 초기회되어있다고 가정.
        return f[n]
      else:
        f[n] = f[n-2] + f[n-1] # 중간 계산 결과를 caching.
        return f[n]
      
  </code>
</pre>
     
     
**bottom-up 방식**
<pre>
  <code>
    def fib(n):
      f[1], f[2] = 1, 1
      for i in range(3, n+1):
        fib[i] = fib[i-1]+fib[i-2]
      return fib[n]
  </code>
</pre>
      
또 다른 예로 이항
