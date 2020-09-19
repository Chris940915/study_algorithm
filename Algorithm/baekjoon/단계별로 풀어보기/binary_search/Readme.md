

선형구조 부분탐색법인 이분탐색은 찾고자하는 값이 없으면 탐색이 실패한다.    
이를 방지하기 위하여 두가지 방법이 있다.

## Lower bound
찾고자 하는 값 **이상**이 처음으로 나타나는 위치.   
찾고자 하는 값 이상의 값이 처음으로 나타나는 위치를 찾아내기 위해, 이분 탐색의 조건을 조금 변경하면 된다.   

<pre>
  <code>
    def lower_bound(upper, lower, target):
       while lower <= upper:
          mid = (lower+upper)//2
          
          if target <= mid:
              upper = mid + 1
          else:
              lower = mid - 1
       return upper
       
  </code>
</pre>


## Upper bound    
찾고자 하는 값 **초과하는 값**이 처음으로 나타나는 위치.    
    
<pre>
  <code>
    def lower_bound(upper, lower, target):
      while lower <= upper:
        mid = (lower+upper)//2
        
        if target < mid:
            upper = mid + 1
        else:
            lower = mid - 1
  </code>
</pre>
