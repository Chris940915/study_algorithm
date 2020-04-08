
map reduce 를 사용하면서 잘 모른다니....

일단 mapreduce에 대해서 짚고 넘어간 후, python 의 map,filter,reduce에 대해 알아보자. 
    
맵리듀스의 예제로 가장 쉽게 생각 가능한 것은 wordcount !!    
**map** 을 통해 한 줄씩 읽어가면서 단어를 잘라 만든다.   
그리고 각 단어의 value를 1로 해서 차곡차곡 **나열한다.**   
빅데이터 처리 프레임워크는 **suffling** 이라는 작업을 통해 비슷한것끼리 모아서 정리를 해준다.     
이어서 **reduce** 작업이 돌아가서 같은 키들끼리 value를 더해 최종적으로 단어별 출현 빈도를 집계한다.    
이렇게 빅데이터를 처리하기 위해서 단순화한 패턴 (모든 value를 1로 초기화 후, 키를 중심으로 집계)을 사용하게 된다.   
        
파이썬에서 map, reduce 그리고 filter를 이제 알아보자.    


## map    
map의 경우, list의 element에 함수를 적용시켜 결과를 반환하고 싶을 때 사용한다.     
만약, 어떤 리스트의 원소를 제곱한 새로운 리스트를 만들고 싶다면, 일반적인 C언어 스타일의 해결법은 다음과 같다.    

<pre>
  <code>
    items = [1, 2, 3, 4, 5]
    squared = [ ]
    for i in items:
      squared.append(i**2)
      
  </code>
</pre>
하지만 map function을 통해 위 코드를 짧게 구현할 수 있다.    
**map(fuction, iterable)** 로 **iterator**를 리턴한다.    
    
<pre>
  <code>
    items = [1, 2, 3, 4, 5]
    squared = list(map(lambda x: x**2, items))
  </code>
</pre>
    
이러한 map 함수 표현식은 for 루프 스타일(List Comprehension)로 만들 수 있다.    
<pre>
  <code>
    items = [1, 2, 3, 4, 5]
    squared = [ i**2 for i in items ]
  </code>
</pre>

dictionary도 map 대신 List Comprehension으로 만들 수 있다.    
<pre>
  <code>
    {k:v**2 for k, v in dict_items.items()}
  </code>
</pre>
    
아무래도 이렇게 리스트 컴프리헨션으로 쓰는게 파이썬틱한 스타일일까??    
그렇지만 이렇게 짠다면 새로운 리스트가 무조건 생기게 되며, map 함수로 코드를 짠다면 list()로 변환을 안시키면 iterator 이기 때문에 메모리상 이점이 있다.   
    
## filter   
filter는 일반적으로 리스트의 일부 아이템을 걸러낼 떄 사용하는 함수.   
(As the name suggets, filter creates a list of elements for which a function returns trure.)    
    
아래와 같이 사용할 수 있다.    
<pre>
  <code>
    input = [1, 2, 3, 4, 5]
    even = list(filter(lambda x: x % 2 == 0, input))
  </code>
</pre>

map 함수와 마찬가지로 filter 함수의 결과도 iterator를 리턴한다.    

<pre>
  <code>
    input = [1, 2, 3, 4, 5]
    even = [i for i in input if i%2 == 0] 
  </code>
</pre>
또한, List Comprehension으로 표현할 수 있다.

## reduce   
reduce는 Python3 부터 built-in 함수가 아니라서 모듈을 import 해줘야한다.    
어떤 list에 대해서 computation을 해서 결과를 내보낼 때, 즉 결과를 어떤 함수로 computation해서 축약하기 위해서 사용한다.   
이 때, reduce 함수에 input으로 들어가는 함수는 두 element를 연산하는 로직을 넣어야한다.   
따라서 List Comprehension으로 표현할 수 없다.    

<pre>
  <code>
    from functools import reduce
      reduce(lambda x,y: x+ y, input)
  </code>
</pre>

input 리스트에서 하나씩 다 더하는.....    

더 구체적으로 접근해보자.    
1~100까지 합을 구하는 3가지 방법이 있다.    

<pre>
  <code>
    # C언어 스타일.
    sum_v = 0
    for i in range(1, 101):
      sum_v += i
  
    # Python 스러운 스타일. 
    sum_v = reduce(lambda x,y: x+y, [x for x in range(1, 101)])
    
    # 하지만 더 발전... 
    import numpy as np  
    np.sum([x for x in range(1, 101)])
    
  </code>
</pre>
