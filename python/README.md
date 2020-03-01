python에 대하여 알아보자. 


[함수 인자 전달 방식](#함수-인자-전달-방식)
   
[list, tuple, set, ditonary](#list,tuple,set,dictionary)   
[- list](#list)   
[- tuple](#tuple)   
[- set](#set)

---------------------------------------

# 함수 인자 전달 방식

크게 2가지가 있다.

1. Call by value - 값에 의한 호출

2. Call by reference - 주소(참조)에 의한 호출   
   
하지만, python은 두가지에 다 해당되지않고 Call by object reference (객체 참조에 의한 호출)에 해당한다. 

python은 기본적으로 변수를 메모리 주소에 저장하는 것이 아니라 변수에 객체를 할당한다.   

https://yes90.tistory.com/47


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
      # 얕은 복사의 경우, 메모리 주소는 다르게 할당되지만 요소를 변경할 경우 같이 변경된다.
     
      full_slice == s
      #True
      
      s is full_slice
      #False
      
      s[0] = 3
      # full_slice = [3,0,0,0,0]
      
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
 
## tuple
   
tuple은 **immutalbe한 순서가 있는 객체의 집합.**   
따라서, 리스트와 같이 내용을 변경하는 append 같은 메서드는 사용할 수 없고, *요소의 정보를 구하는 메서드만 사용 가능.*   
   
순서가 있기 때문에 list와 같이 인덱스로 접근 가능.   

* tuple은 사실 '(, )'가 필요없다.   
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
      
   

