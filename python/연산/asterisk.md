파이썬의 Asterisk(\*) 을 잡아보자. 
    
파이썬은 타 언어에 비해 연산자 및 연산의 종류가 풍부한 편.    
Asterisk(\*)로 할 수 있는 여러 연산들이 존재.    
    
사용되는 경우를 크게 4가지로 구분할 수 있다.    
    
* 곱셉 및 거듭제곱 연산으로 사용할 때    
* 리스트형 컨테이너 타입의 데이터를 반복 확장하고자 할 때   
* 가변인자 (Variadic Arguments)를 사용하고자 할 때    
* 컨테이너 타입의 데이터를 Unpacking 할 때     

## 곱셉 및 거듭제곱 연산으로 사용할 때     
    
곱셉 연산으로 사용할 수 있으며, 파이썬은 거듭제곱 연산까지 지원.     

<pre>
  <code>
    2 * 3   
    # 6   
    
    2 ** 3
    # 8
  </code>
</pre>
      
## 리스트형 컨테이너 타입의 데이터를 반복 확장하고자 할때     
    
파이썬에서는 \*을 숫자형 데이터 뿐만 아니라 리스트형 컨테이너 타입에서 데이터를 반복적으로 확장하기 위해 사용할 수도 있다.    
    
<pre>
  <code>
    zero_list = [0] * 100
    
    zero_tuple = (0,) * 100
    
    vector_list = [[1,2,3]]
    
    for i, vector in enumerate(vector_list * 3):
      print([(i+1) * e for e in vector])
    
    # [1,2,3]
    # [2,4,6]
    # [3,6,9]
    
  </code>
</pre>
    
    
## 가변인자 (Varidic Parameters)를 사용하고자 할 때     
    
우리는 종종 어떤 함수에서 가변인자를 필요로 할 때가 있다.   
예를 들어, 들어오는 인자의 갯수를 모른다거나, 그 어떤 인자라도 받아서 처리해야할 떄.   
        
파이썬에서 인자의 종류가 2가지가 있다.    
**positional arguments** 와 **keyword arguments** 이다.    
positional arguments는 위치에 따라 정해지는 인자이고, keyword arguments는 키워드를 가진, 이름을 가진 인자를 의미.    
      
가변인자는 위의 두가지 인자로 모두 사용할 수 있으며, 사용 방법은 다음과 같음.   

#### positional arguments만 받을 때   
<pre>
  <code>
    def save_ranking(*args):
      print(args)
    save_ranking('ming', 'alice', 'tom', 'wilson', 'roy')
    # ('ming', 'alice', 'tom', 'wilson', 'roy')
  </code>
</pre>
    
    
#### keyword arguments만 받을 때   
<pre>
  <code>
    def save_ranking(**kwargs):
      print(args)
    save_ranking(first='ming', second='alice', fourth='wilson', third='tom', fifth='roy')
    # ('first': 'ming', 'second': 'alice', 'fourth': 'wilson', 'third': 'tom', 'fifth': 'roy')
  </code>
</pre>
    
#### positional arguments와 keyword arguments를 모두 받을 때   
<pre>
  <code>
    def save_ranking(*args, **kwargs):
      print(args)
      print(kwargs)
    save_ranking('ming', 'alice', 'tom', fourth='wilson', fifth='roy')
    # ('ming', 'alice', 'tom')
    # {'fourth': 'wilson', 'fifth': 'roy'}
  </code>
</pre>
       
\*args 는 임의의 개수의 positional arguments를 받음을 의미하며, \*\*kwargs는 임의의 개수의 keyword arguments를 받음을 의미.   
이 때 \*args, \*\*kwargs 형태로 가변인자를 받는 것을 **packing** 이라고 한다.    
    
위의 결과에서 볼 수 있듯이, positional 형태로 전달되는 인자들은 args 라는 **tuple**에 저장되며,    
keyword 형태로 전달되는 인자들은 kwargs 라는 **dict**에 저장된다.   
    
positional과 keyword의 선언 순서는 keyword가 무조건 뒤에 있어야 하므로, kwargs도 args의 앞에 있을 수 없다.    

*args 이나 kwargs를 관례적으로 사용하지만, \*required 나 \*\*optional 과 같이 인자명을 일반 변수와 같이 지정 가능하다.*     
    
## 컨테이너 타입의 데이터를 Unpacking 할 때    
    
\* 는 컨테이너 타입의 데이터를 Unpacking 하는 경우에도 사용할 수 있다.    
이는 3번과 유사한 원리로, 종종 사용할만한 기능.      

<pre>
  <code>
    from functools import reduce
    
    primes = [2, 3, 5, 7, 11, 13]
    
    def product(*numbers):
      p = reduce(lambda x, y: x * y, numbers)
      return p
    
    product(*primes)
    # 30030
    product(primes)
    # [2, 3, 5, 7, 11, 13]
    
  </code>
</pre>
         
product 함수가 가변인자를 받고 있기 때문에 우리는 리스트의 데이터를 모두 unpacking 하여 함수에 전달해야한다.     
이 경우 함수에 값을 전달할 때 \*primes와 같이 전달하면 primes 리스트의 모든 값들이 unpacking 되어 numbers 라는 리스트에 저장된다.   
만약 이를 primes 그대로 전달한다면 이 자체가 하나의 값으로 쓰여 numbers 에는 primes 라는 원소가 하나 존재하게 된다.      
    
tuple 도 list와 동일하게 동작하며 dictionary의 경우 \* 대신 \*\*를 사용하여 동일한 형태로 사용할 수 있다.   
    
<pre>
  <code>
    tweet = {
      "usernameTweet" : "social",
      "ID" : "1202030",
      "text" : "Hi, my name is hansub"
    }
    
    def pre_process(**tweet):
      result = ''
      id = tweet['ID']
      
      text = tweet['text']
      if 'RT' not in text:
        continue
      else:
        result = text
      return result
    
    pre_process(**tweet)
  </code>
</pre>
    
    
### 참고   
    
또 다른 형태의 unpacking이 한 가지 더 존재하는데, 이는 함수의 인자로써 사용하는게 아닌 리스트나 튜플 데이터를 다른 변수에 가변적으로 unpacking 하여 사용하는 형태.    

<pre>
  <code>
    numbers = [1, 2, 3, 4, 5, 6]
    # unpacking의 좌변은 리스트 또는 튜플의 형태를 가져야하므로 단일 unpacking의 경우 *a가 아닌 *a,를 사용
    *a, = numbers
    # a = [1, 2, 3, 4, 5, 6]

    *a, b = numbers
    # a = [1, 2, 3, 4, 5]
    # b = 6

    a, *b, = numbers
    # a = 1
    # b = [2, 3, 4, 5, 6]

    a, *b, c = numbers
    # a = 1
    # b = [2, 3, 4, 5]
    # c = 6
  </code>
</pre>
    
여기서 \*a, \*b로 받는 부분들은 우변의 리스트 또는 튜플이 unpacking 된 후, 다른 변수들에 할당된 값 외의 나머지 값들을 다시 하나의 리스트로 packing 한다.    

