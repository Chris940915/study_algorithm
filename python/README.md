python에 대하여 알아보자. 

   
[list, tuple, set, ditonary](#list,tuple,set,dictionary)   
[- list](#list)   
[- tuple](#tuple)   
[- set](#set)   
[- dictionary](#dictionary)   
   
[함수 인자 전달 방식](#함수-인자-전달-방식)   
   
[Collection 모듈](#Collection)   
   
[제곱,제곱근](#제곱,)

------------------------------------
   
   
# list,tuple,set,dictionary
   
리스트, 튜플, 셋, 딕셔너리는 모두 각각의 특징과 차이점에 따라 쓰임새가 다르다.   
볼때마다 헷갈리므로 이번 기회에 정리를 하여 명확하게 해보자.
   
## list

list는 **mutable한 순서가 있는 객체 집합**으로 python의 list는 기본적으로 **동적배열**이다.  
또한, python의 문자열은 list로 나타낼 수 있지만 immutable하다는 점을 명심하자.   


<pre>
<code>
   a = [1,2,3]
   id(a)
</code>
   -> 439788808
   
<code>
   a[0] = 5
   a
</code>
   -> [5,2,3]
<code>
   id(a)
</code>
   -> 439788808
</pre>
   
a에 1,2,3을 원소로 가지는 리스트를 할당.   
id()는 변수의 메모리 주소값을 리턴.   
a의 첫번째 원소를 변경한 후에도 **id값은 변경없이 a의 변수가 변경된다.**   
   
리스트를 합치는 것은 + 연사자로 간편하게 가능.      
   
python의 list에서 중요한 점 중 하나는 **인덱싱, 슬라이싱**이다.   
다른 언어에서는 마지막열을 찾기위해 리스트의 길이를 구해서 찾아야 하지만, 파이썬은 -1만으로도 손쉽게 찾을 수 있다.   
슬라이싱을 통해서 새로운 리스트를 만드는 것도 가능하다.   
   
<pre>
   <code>
      s = [0,0,0,0,0]
      full_slice = s 
      s is full_slice
      #True
      
      full_slice[0] = 2
      # s = [2,0,0,0,0]
      
      #full_slice와 s는 변수 이름만 다를 뿐 같은 객체이다.   
      # 따라서, 다른 방법으로 리스트를 복사할 필요가 있다.   
   
      # 리스트의 복사도 얕은 복사와 깊은 복사 2가지로 나뉜다.
         
      #1
      full_slice = s[:]
      
      #2
      full_slice = s.copy()
      
      # 위 2가지 경우에는 얕은 복사에 해당한다.
      # 얕은 복사의 경우, 메모리 주소는 다르게 할당되고 요소를 변경하면 함께 변경되지 않는다.
     
      full_slice == s
      #True
      
      s is full_slice
      #False
      
      s[0] = 3
      # full_slice = [2,0,0,0,0]
      
      # 깊은 복사도 있다.   
      
      import copy
      
      #1
      full_slice = list()
      for i in s:
         full_slice.append(i)
      
      #2 
      full_slice = copy.deepcopy(s)
      
   </code>
</pre>
   
   
또한, 리스트를 거꾸로 하는 것도 step을 사용하여 가능.
   
<pre>
   <code>
      reverse_slice = s[::-1]
   </code>
</pre>
   
리스트는 기본적으로 맨 뒤에 추가, 삭제를 할 수 있으며 다양하게 응용 가능.   

<pre>
   <code>
      # 리스트에 요소 추가.
      
      a = [10,20,50]
      a.append(30)
      # a = [10,20,50,30]
      
      a.insert(1, 40)
      # a = [10,40,20,50,30]
      
      # 리스트에 요소 삭제.   
      a = [10, 20, 30]
      a.pop()
      # 30
      a.pop(0)
      # 10
      # a = [20]
      a = [10, 20, 30]
      del a[0]
      # a = [20, 30]
      
      a = [20, 30, 20]
      a.remove(20)
      # a = [30, 20]
   </code>
</pre>
   
remove는 해당하는 값을 삭제하면 맨 처음 나타나는 값을 삭제한다.   
pop(0)의 경우, 맨 앞에 요소를 삭제하고 뒤에 모든 요소들을 앞으로 한칸씩 당겨오므로 O(n)이 소요된다.   
따라서, pop(0)가 아니라 deque 모듈을 사용하여 popleft() - O(1)를 사용하는 것이 효율적이다.   
    
*리스트를 이용하여 스택(stack)과 큐(queue)를 구현할 수 있다.*   

   
list 내의 모든 원소들의 자료형을 변경할때는 map() 사용.   
map()은 리스트의 원소를 지정된 함수로 처리해주는 함수로 원본 리스트를 변경하지 않고 새 리스트를 생성.
   
   
#### 2차원 리스트를 1차원 리스트로 만들기    
2차원 리스트를 1차원 리스트로 만들때 어떻게 해야할까.   
다른 언어에서는 보통 반복문을 이용해 리스트를 더한다.

<pre>
   <code>
      my_list = [[1,2], [3,4], [5,6]]
      answer = []
      for i in my_list:
          answer += i
   </code>
</pre>
   
파이썬의 다양한 기능을 사용하면, for 문을 사용하지 않고도 리스트를 이어붙일 수 있다.   

<pre>
   <code>
      my_list = [[1,2], [3,4], [5,6]]
      
      #방법 1 - sum 
      answer = sum(my_list, [])
      
      #방법 2 - itertools.chain
      import itertools
      list(itertools.chain.from_iterable(my_list))
      
      #방법 3 - itertools와 unpacking
      import itertools
      list(itertools.chain(*my_list))
      
      #방법 4 - list comprehension 이용
      [element for array in my_list for element in array]
      
      #방법 5 - reduce 함수 이용
      from functools import reduce
      list(reduce(lambda x,y: x+y, my_list))

   </code>
</pre>

 
## tuple
   
tuple은 **immutalbe한 순서가 있는 객체의 집합.**   
따라서, 리스트와 같이 내용을 변경하는 append 같은 메서드는 사용할 수 없고, *요소의 정보를 구하는 메서드만 사용 가능.*   
   
순서가 있기 때문에 list와 같이 인덱스로 접근 가능.   

* tuple은 사실 '(, )'가 필요없다.   
* tuple은 하나의 원소만을 가질 수 없다.
  대신, 하나의 원소만을 가질때는 ',' 를 붙여서 표현한다.
  ex) (3,)
* tuple을 이용하여 함수에서 여러 값을 한꺼번에 리턴시킬 수 있다.   

<pre>
   <code>
      def minmax(items):
         return min(items), max(items)
     
      minmax([7,5,1,11,55])
      
      >> (1,55)
   </code>
</pre>
   
* 특정 값의 인덱스 구하기. 

<pre>
   <code>
      a = (38,21,53,19,53)
      a.index(53)
      >> 2
   </code>
</pre>
   
   
## set
set은 수학의 집합과 비슷하여 **mutable하며 순서가 없고 unique한 값을 가진다.**   
중괄호를 사용하는 것은 dictionary와 비슷하지만, key가 없고 value만 존재한다.      

* set(집합)의 원소 추가
   원소 추가는 add 메소드를 사용한다.
   
<pre>
<code>
   k = {100, 105}
   k.add{50)
   
   #k = {100, 105, 50}
   
</code>
</pre>

* set의 update
   set은 중복은 자동 제거되고 수정이라는 개념보다 여러데이터를 한번에 추가할 때 사용.   
   
<pre>
<code>
   k = {1, 2, 3}
   k.update([3,4,5])
   
   #k = {1, 2, 3, 4, 5}
</code>
</pre>

<pre>
   <code>
      a = {1, 2, 3, 4}
      b = a.copy()
      
      a is b
      #False
      
      a == b 
      #True
      
      b.add(5)
      #a = {1, 2, 3, 4}
      #b = {1, 2, 3, 4, 5}
      
   </code>
</pre>


## dictionary
dictionary은 **mutable하며 순서가 없는 key, value으로 맵핑되어 있는 집합이다.**

* 키로는 immutable한 값은 사용할 수 있지만, mutable한 값은 사용할 수 없다.   
* 값(value)는 중복될 수 있지만, 키(key)가 중복되면 마지막 값으로 덮어씌워진다.   
* mutable한 객체이므로 키로 접근하여 값을 변경할 수 있다.       
   
* 단일 수정은 키로 접근하여 값을 할당.
<pre>
   <code>
      a = {'alice':[1,2,3], 'bob':20}
      a['alice'] = 5 
      #a = {'alice':5, 'bob':20}
   </code>
</pre>
   
* 여러 값 수정은 update 메소드를 사용한다. 키가 없는 값이면 추가된다.   
<pre>
   <code>
      a = {'alice':[1,2,3], 'bob':20}
      a.update({'bob':99, 'tony':99})
      #a = {'alice':[1,2,3], 'bob':99, 'tony':99}
   </code>
</pre>
   
   
* dictionary for 문   
   for 문을 통해 dictionary를 돌리면 Key값이 할당된다.  
   순서는 임의적이며, 같은 순서를 보장하지 않는다.   
   <pre>
      <code>
         a = {'alice':[1,2,3], 'bob':20}
         for key in a:
            print(key)

         # alice
         # bob

      </code>
   </pre>
   
   value 값으로 for문을 반복하기 위해서는 **values()** 를 사용한다.   
   <pre>
      <code>
         for val in a.values():
            print(val)
         
         # [1,2,3]
         # 20
      </code>
   </pre>
   
   key 와 value를 한꺼번에 for문을 반복하려면 **items()** 를 사용한다.   
   <pre>
      <code>
         for key, val in a.items():
            print(key, val)
         
         # alice [1,2,3]
         # bob 20
      </code>
   </pre>
   
---------------------------------------

# 함수 인자 전달 방식

크게 2가지가 있다.

1. Call by value - 값에 의한 호출

2. Call by reference - 주소(참조)에 의한 호출   
   
하지만, python은 두가지에 다 해당되지않고 Call by object reference (객체 참조에 의한 호출)에 해당한다. 

python은 기본적으로 변수를 메모리 주소에 저장하는 것이 아니라 변수에 객체를 할당한다.   

https://yes90.tistory.com/47
https://zzonglove.tistory.com/21



   
---------------------------------------

# Collection 








---------------------------------------
# 제곱,제곱근
   
math 모듈에서 pow()와 sqrt()를 제공.    
모듈 대신에 곱 연산자 2개를 사용해서도 사용 가능.

<pre>
   <code>
      import math
      
      # a^n 
      a_n = a**n
      math.pow(a, n)
   
   </code>
</pre>

제곱근의 경우 반대로 생각하면 되며, 완전제곱수인지 판별할 수 있다.

<pre>
   <code>
      import math
      
      a_n = a**0.5
      math.sqrt(a,2)
      
      def check(x):
         temp = x**0.5
         
         # 완전제곱수면 뒤에 소숫점이 없음.
         if int(temp) == temp:
            #예외의 경우가 발생하므로 제곱하여 확인. 
            if temp**2 == x:
               return True
         return False
       
   </code>
</pre>


