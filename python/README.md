python에 대하여 알아보자. 

[함수 인자 전달 방식](#함수-인자-전달-방식)   
[- 얕은 복사, 깊은 복사](#얕은-복사-깊은-복사)   
   
[Collection 모듈](#Collection)   
   
[제곱,제곱근](#제곱)

------------------------------------
   
  

# 함수 인자 전달 방식

크게 2가지가 있다.

1. Call by value - 값에 의한 호출

2. Call by reference - 주소(참조)에 의한 호출   
   
하지만, python은 두가지에 다 해당되지않고 Call by object reference (객체 참조에 의한 호출)에 해당한다. 

python은 기본적으로 변수를 메모리 주소에 저장하는 것이 아니라 변수에 객체를 할당한다.   

https://yes90.tistory.com/47
https://zzonglove.tistory.com/21
      
mutable object들은 Call by reference 형식으로 불리면, object가 전달되기 전의 원본(변수) 자체를 바꿀 수 있다.   
   
<pre>
   <code>
      def updateList(list1):
         list1 += [10]
      
      n = [5, 6]
      print(id(n)) # 140312184155336
      updateList(n)
      print(n)     # [5, 6, 10]
      print(id(n)) # 140312184155336
   </code>
</pre>
   
위의 예제를 보면, **Call by reference**를 이용해서 list인 n을 불러냈고 list 자체가 변경되었다.   
   
<pre>
   <code>
      def updateNumber(n):
         print(id(n))
         n += 10
      b = 5
      print(id(b))      #1055680
      updateNumber(b)   #1055680
      print(b)          #5
   </code>
</pre>
   
위의 예제에서는 object가 전달되지만 바뀌지 않는다.   
하지만, 함수 안에서의 n과 밖에서의 b는 id()를 통해 확인한 것 처럼 서로 같은 주소값을 지칭하고 있다.   
그럼에도 불구하고 n += 10 에서 바뀌지 않는 이유는 **pass by value** 이기 때문이다.   
말 그대로 함수에 의해 어떤 값(n)이 필요해질때 object 자체를 전달하지 않고 변수의 '값'만 전달한 것이다.      
**그래서 변수가 참조하는 object는 변하지 않았지만, 함수 범위 내에서의 object 자체는 변했습니다.**   
   
immutable한 int object를 함수에서 호출해도 어차피 int 자료형은 immutable하므로 바뀌지 않는다.    
따라서 값(value)만 넘겨주고 함수 범위(scope)내에서 새로운 object를 만드는 것이 더 편한 방법.   
immutable은 **call by value**, mutable은 **call by reference**를 사용하는 것이 일반적.   

## 얕은 복사 깊은 복사   
   
객체의 복사는 크게 얕은 복사(shallow copy)와 깊은 복사(deep copy)로 나뉩니다.   
어려운 개념은 아니지만 주의해서 사용해야한다.   
   
1. 단순 객체 복제.
   
변수만 복사하다 보니 바라보는 객체는 당연히 동일하다.   
즉, 두개의 변수 중 하나만 변경되어도 나머지 하나는 동일하게 수정되는 현상이 발생.   
   
<pre>
   <code>
      a = [1,2,3,4]
      b = a
      print(b) # [1,2,3,4]
      b[2] = 100
      print(b) # [1,2,100,4]
      print(a) # [1,2,100,4]
      
   </code>
</pre>
   
a는 리스트 객체의 주소를 바라보는 변수.   
그런 뒤 a를 b에 할당하면, b는 a와 같은 객체의 주소를 바라보게 된다.   
   
a 또는 b를 수정하면 문제가 발생한다.   
b의 3번째 값을 변경하면 a 또한 b와 같이 수정되어버린다.   
이는 a와 b가 동일한 객체를 참조하기 때문에 발생하는 문제.   
   
* 위의 경우처럼 복사된 참조 변수를 수정했을때, 처음에 할당한 참조 변수의 값 역시 똑같이 수정되는 것은 **리스트와 같은 변경가능(mutable) 객체일떄만 해당한다.**     
숫자나 문자열과 같은 불변의(immutable)객체일때는 위의 경우가 해당되지 않는다.   

<pre>
   <code>
      a = 10
      b = a
      print(b) # 10 
      b = 'abc' 
      print(b) # abc
      print(a) # 10
   </code>
</pre>
  
불변의 객체이기 때문에, 참조변수를 수정한다는 것은 주소의 값(value)이 바뀌는 것이 아니라 그 변수에 새로운 객체가 할당되는 것을 뜻한다.   
   
2. 얕은 복사(Shallow copy)   
   
얕은 복사는 단순 복사와 어떤 차이가 있을까?   
단순 복사와 얕은 복사의 차이점은 복합객체(리스트)는 별도로 생성하지만, **그 안에 들어가는 내용은 원래와 같은 객체라는 점** 입니다.   
   
<pre>
   <code>
      import copy

      a = [1, [1,2,3]]
      
      b = copy.copy(a)
      print(b) #[1, [1,2,3]]
      b[0] = 100
      print(b) #[100, [1,2,3]]
      print(a) #[1, [1,2,3]]
      
      c = copy.copy(a)
      c[1].append(4)
      print(c) # [1, [1,2,3,4]]
      print(a) # [1, [1,2,3,4]], a가 c와 똑같이 수정된 이유는 리스트의 item 내부의 객체는 동일한 객체이므로 mutable한 리스트를 수정할때는 두 값이 변경됨.   
   </code>
</pre>
   
리스트 내에 리스트가 있는 경우에 얕은 복사(b = copy.copy(a))가 이뤄지더라도 리스트 내의 내부 리스트까지 별도의 객체로 복사가 되는것은 아닙니다.   
위의 예제에서 b의 첫번째 요소(int)를 변경하였을때 a가 변경되지 않은 것은 요소(int)가 immutable 하기 때문입니다.   
   
그러나 c의 경우는 좀 다르다.   
a를 복사하여 c를 만들지만, c의 두번째 요소(list)는 mutable하기 때문에 c의 내부 리스트를 수정하면 a의 내부리스트 또한 바뀌게 된다.   
그 이유는 a와 c의 내부리스트는 같은 객체를 참조하기 때문이다.   
   
3. 깊은 복사(deep copy)   
   
mutable 한 내부객체(list와 같은..)의 문제를 해결하기 위해서는 얕은 복사가 아닌 깊은 복사(deep copy)를 해야한다.   
얕은 복사가 복합객체(list)만 복사되고 그 안의 내용은 동일한 객체를 참조한다면, 깊은 복사의 경우에는 복합객체를 새롭게 생성하고 그 안의 내용까지 재귀적으로 새롭게 생성한다.   
   
**그래서 깊은 복사를 하게 되면, 처음에 만들었던 객체와 복사된 객체가 전혀 달라지기 때문에 어느 한쪽을 수정한다고 해서 다른 한쪽이 영향을 받지 않는다.**
   
   
---------------------------------------

# Collection 
https://docs.python.org/3/library/collections.html#module-collections

### deque 
덱은 double-ended queue의 줄임말로 앞과 뒤, 양방향에서 데이터를 처리할 수 있는 queue형 자료구조를 의미한다.   
list-like container with **fast appends and pops on eiter end**   
   
python의 list와 비슷하지만, 시간복잡도가 O(1)인 popleft(), appendleft()함수를 지원한다.   
   
   
### Counter
*hash가능한 객체를 카운트하는 **dict***	  
데이터의 개수를 셀 때 유용한 클래스.   
   
* dictionary를 이용한 카운팅
<pre>
   <code>
      def countLetter(word):
         counter = {}
         for letter in word:
            if letter not in counter:
               counter[letter] = 0
            counter[letter] += 1
         return counter
         
      countLetters('hello world')
      # {'h': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'w': 1, 'r': 1, 'd': 1}
   </code>
</pre>
   
하지만, 이 코드를 Counter 클래스가 한 줄로 줄여준다.   
   
<pre>
   <code>
      from collections import Counter
      
      Counter('hello world') # Counter({'h': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'w': 1, 'r': 1, 'd': 1})
   </code>
</pre>
   
또한, 주어진 단어에서 가장 많이 등장하는 알파벳과 그 알파벳의 개수를 구하는 함수는 다음과 같이 작성할 수 있다.   
   
<pre>
   <code>
      from collections import Counter
      
      def find_max_alpha(word):
         counter = Counter(word)
         max_count = -1
   
         for letter in counter:
            if counter[letter] > max_count:
               max_count = counter[letter]
               max_letter = letter
         return max_letter, max_count
   </code>
</pre>
   


### OrderedDict
*순서가 있는 Dictionary*   
파이썬의 딕셔너리는 순서를 관리하지 않는다.   
**예를 들어, a, b, c 순으로 입력해도 a, b, c 순으로 출력되지 않는다.**   
   
하지만, OrderedDict은 입력된 순서대로 key의 순서를 유지한다.
   
   
### defaultdict
dict subclass that calls a factory function to supply missing values   
딕셔너리를 만드는 dict 클래스의 서브클래스.   
작동방식은 거의 동일한데, defaultdict()은 인자로 주어진 객체의 기본값을 딕셔너리 값의 초깃값으로 지정할 수 있다.   
숫자, 리스트, 셋 등으로 초기화 할 수 있기 때문에 여러 용도로 사용할 수 있다.(밑의 default 값에 int 대신에 list, set 등을 줄 수 있다.)      

<pre>
   <code>
      from collections import defaultdict
      
      int_idct = defaultdict(int)
      
      int_dict['key_1'] # defaultdict(<class 'int'>, {'key_1' :0})
      
   </code>
</pre>

   
### namedtuple
*tuple타입 subclass를 만들어주는 함수*   
Named tuples assign meaning to each position in a tuple and allow for more readable, self-documenting code.    
They can be used wherever regular tuples are used, and they add the ability to access fields by name instead of position index.
    
튜플은 항목에 인덱스(index)로 접근하므로 직관적이지 않다.   
   
* 튜플의 방식 - mytuple[0], mytuple[1], ... 이렇게 하면 0번째, 1번째 항목에 대한 정보를 구체적으로 알 수 없다.    
   
*하지만, 네임드튜플은 mytuple.age, mytuple.birth, 와 같이 사용자가 항목에 이름을 붙여 사용할 수 있다.*   
   
<pre>
   <code>
      from collections import namedtuple
      Ex = namedtuple("card", "name age phone_num")
      John_Card = Ex("John", 30, "010-2222-2222")
      
      John_Card.name # John
      John_Card.age  # 30
      John_Card.phone_num # 010-2222-2222
      
   </code>
</pre>
   
namedtuple 함수가 반환하는 값은 **클래스(Class)** 다. 위의 클래스는 card 라는 이름을 가진 Ex라는 클래스를 만들어낸다.   
언뜻보면, Ex라는 클래스의 이름이 card와 Ex 두개를 가지고 있는 것처럼 보인다.   
따라서, card = namedtuple("card", "name age phone_num") 처럼 동일하게 선언할 필요가 있다.   
또한, 주의할 점은 John_Card로 선언된 네임드 튜플 객체는 클래스부터 만들어졌지만 튜플처럼 속성을 변경하거나 추가할 수 없다.   
   
   

---------------------------------------
# 제곱
   
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


