python에 대하여 알아보자.


python은 Cpython....

    
## 효율적인 파이썬 작성    

*1. 내장함수(built-in fuctions)를 사용하라.   

https://docs.python.org/3/library/functions.html

2. 긴 문자열을 합칠때는 **join()**을 사용하라.    
여러 문자열들을 합칠 때 "+"를 보통 사용한다.   
파이썬에서 String 은 immutable 하기 때문에, "+" 연산을 할 대 새 문자열을 만들고 기존 내용을 복사한다.    
그러므로 **join()**이 효율적이다.   

<pre>
  <code>
    for chunk in input():
      my_string.join(chunk)
  </code>
</pre>

3. 변수를 swap할 때는 다중할당을 사용하라.   
<pre>
  <code>
    x, y = y, x
   
  </code>
</pre>
    
4. 가능하면 지역 변수를 사용하라.   
파이썬은 전역 변수를 검색하는 것보다 지역 변수를 검색하는 것이 빠르다.    
"global" 키워드를 사용하지 마라.    
    
5. 가능하면 **in** 을 사용하라.    
일반적으로 원소인지 확인하기 위해선 **in** 을 사용하자.    

<pre>
  <code>
    if key in sequence:
      print("found")
  </code>
</pre>
    
6. 무한루프를 생성한다면 **while 1** 을 사용하라.    
while True: 보다 한 단계 빠른 방법.    
<pre>
  <code>
    while 1:
      
    while True:
  </code>
</pre>
    
7. List Comprehension을 사용하라.    
List Comprehension은 파이썬 인터프리터가 루프를 돌면서 예측 가능한 패턴을 발견할 수 있게 최적화되어 있어서 더 빠르다.   
또한 List Comprehension은 가독성이 뛰어나고, 대부분의 경우 카운팅을 위한 하나의 변수만을 저장.    

<pre>
  <code>
    # 파이썬스러운 방법
    evens = [i for i in range(10) if i%2 == 0]
    
    # 파이썬스럽지 않은 방법
    i = 0
    evens = []
    while i < 10:
      if i%2 == 0: evens.append(0)
      i += 1
  </code>
</pre>

8. 매우 긴 Sequence에는 xrange()를 사용하라.    
**xrange()** 는 한 번에 하나의 정수 원소만 생성하므로 시스템 메모리를 절약할 수 있다.          
range()와 달리 전체 목록을 제공하므로, 루프를 도는 중에 불필요한 overhead가 발생.    
    
9. On demand로 데이터 얻을 때는 파이썬 제너레이터(generator)를 사용하라.   
이 방법은 메모리를 절약할뿐만 아니라 성능을 향상시킬 수 있다.   

<pre>
  <code>
    chunk = (1000 * i for i in xrange(1000))
    
    chunk.next() # 0
    chunk.next() # 1000
    chunk.next() # 2000
  </code>
</pre>

10. itertools 모듈을 배워라.    
itertools 모듈은 iteration과 combination에 굉장히 효율적.      
[1, 2, 3]의 모든 순열을 단 3줄로 생성할 수 있습니다.   

<pre>
  <code>
    import itertools
    iter = itertools.permutations([1,2,3])
    list(iter)
  </code>
</pre>

11. 정렬된 순서로 리스트를 유지하기 위해 **bisect** 모듈을 배워라.    
bisect 모듈은 정렬된 리스트에 원소를 삽입 후, 다시 정렬할 필요 없도록 관리해준다.    

<pre>
  <code>
    import bisect
    bisect.insort(list, element)
  </code>
</pre>

12. 파이썬 리스트(List)는 실제로 배열이라는 것을 명심하자.   
파이썬의 리스트는 일반적인 single-linked list로 구현되지 않는다.    
파이썬에서 리스트는 배열이다(동적배열).    
즉, 처음부터 검색하지 않고 O(1) 동안 indexing을 통해 리스트에서 요소를 검색.    
insert() 를 사용하면 기존 원소들의 index를 모두 변경하기 때문에 비효율적이다.    
    
13. 원소 유무를 확인할 때는 dict와 set을 사용하라.    
파이썬은 dictionary 또는 set 원소가 존재하는지 체크하는 것이 굉장히 빠르다.   
dict 와 set은 **hash table** 로 구현되었기 떄문이다.    
O(1)만큼 빠를 수 있다. 그러므로 존재 유무를 자주 확인해야 될 경우 컨테이너로 dict 또는 set을 사용하십시오.   
<pre>
  <code>
    my_list = ['a', 'b', 'c']
    print('c' in my_list)
    
    myset = set(['a', 'b', 'c'])
    print('c' in myset)
  </code>
</pre>

14. Python decorator    
"@" 기호는 파이썬 decorator 이다. @ 기호는 tracing 뿐만 아니라 locking 이나 logging에도 사용한다.   
나중에 필요한 결과를 기억하도록 Python 함수를 사용할 수 있다. "memoization" 이라고 한다.    

<pre>
  <code>
    from functools import wraps
    
    def memo(f):
      cache = {}
      @wraps(f)
      def wrap(*arg):
        if arg not in cache:
          cache['arg'] = f(*arg)
        return cache['arg']
      return wrap
  </code>
  Fibonacci 함수에 사용할 수 있다.   
  
  <code>
    @memo
    def fib(i):
      if i < 2:
         return 1
      return fib(i-1) + fib(i-2)
  </code>
</pre>

여기서 핵심 아이디어는 간단하다.    
계산한 각 피보나치 항을 기억하도록 decorate하면 된다.    
캐시에 있으면 다시 계산할 필요가 없음.    


ref. https://deepwelloper.tistory.com/113?category=813724
