코딩 문제를 풀다가 알게된 all 과 any에 대하여 알아보쟈.     
잘쓰면 아주 유용하다.    
    
### all(iterable)
**all()** 은 인자로 전달된 모든 값이 True인지 아닌지 확인.    
<pre>
  Return True if all elements of the iterable are ture (or if the iterable is empty. 
    
  <code>
    def all(iterable):
      for element in iterable:
        if not element:
          return False
      return True
  </code>
</pre>
        
*if not element* 부분을 보면 element 중 하나라도 Falsy한 값이 발견되면 바로 함수가 종료되는 것을 확인할 수 있다.    
    

### any(iterable)   
**any()** 는 인자로 전달된 모든 값 중 하나라도 True 가 있는지 확인.      
<pre>
  Return True if any element of the iterable is true. if the iterable is empty, return False.
  
  <code>
    def any(iterable):
      for element in iterable:
        if element:
          return True
      return False
  </code>
</pre>
    
*if element* 부분을 보면 element 중 하나라도 Truthy한 값이 발견되면 바로 함수가 종료되는 것을 확인할 수 있다.     
        
이와 연관되어 있는 것이 **short-circuit evaluation** 이다.      
and/or 연산을 하는데 있어서 첫 번째 인수로 값을 평가하기에 충분하다면 두 번째 인수는 평가하지 않는 것.    

<pre>
  False and True
  True or False
</pre>
    
**False and True** 는 and가 있어서 뒤에 값을 몰라도 False 임을 의미.    
**True or False** 는 or가 있어서 뒤에 값을 몰라도 True 임을 의미.   


Ref. https://velog.io/@doondoony/python-all-any-builtin-functions
