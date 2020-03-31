

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
