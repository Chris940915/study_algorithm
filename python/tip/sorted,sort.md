sorted 와 sort 중에 sorted를 즐겨쓰지만 명확하게 구분하지는 못한다.      
단지, sorted는 새로운 list 객체를 반환한다고만 생각하고 사용했다.      

## list.sort() VS sorted()    

* list.sort()는 리스트 내부에서 정렬된다. 그에 비해, sorted()는 정렬된 값을 돌려준다.   
  그렇기 떄문에 원래 값을 유지하면서 정렬된 결과를 얻고 싶다면 sorted()를 사용하면 된다.     
  list.sort()는 값을 돌려주지 않기 때문에 받게되면 None을 받게 된다.   
    
* list.sort()는 리스트 형에 한해서만 동작하지만, sorted()는 iterable(대부분의 컨테이너)한 자료형에 대해서 동작한다.   
  헷갈리지않게 sorted()로 통일해서 다 사용해야겠다..    
      
### Key Functions   
    
* 둘다 key 파라미터를 가지고 있어 비교의 기준으로 사용할 수 있다.    
  파라미터는 **함수** 여야 하고, 하나의 입력값과 반환값을 가진다.        
  파라미터로 전달된 함수는 입력 레코드마다 한번씩 호출된다.      
  클래스나 복잡한 객체들을 정렬할 때 사용한다.   


Age를 attribtue로 갖는 Studenet 클래스를 선언하고 사용해보자.      
<pre>
  <code>
    sudent_objects = [
      Student('john', 'A', 15),
      Student('jane', 'B', 12),
      Student('dave', 'B', 10),
    ]
    
    sorted(student_objects, key=lambda student: student.age)
  </code>
  [('dave', 'B', 10'), ('jane', 'B', '12'), ('john', 'A', 15)]
</pre>
    
    
### Operator Module Functions   
    
* 파이썬에서 좀더 편하게 사용할 수 있는 접근자 함수를 제공.     
  *itemgetter()* , *attrgetter()* , *methodcaller()*      
    
<pre>
  <code>
    from operator import itemgetter, attrgetter
    sorted(student_tuples, key=itemgetter(2))    
    -> [('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]

    sorted(student_objects, key=attrgetter('age'))   
    -> [('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]

    sorted(student_tuples, key=itemgetter(1,2))    
    -> [('john', 'A', 15), ('dave', 'B', 10), ('jane', 'B', 12)]

    sorted(student_objects, key=attrgetter('grade', 'age'))   
    -> [('john', 'A', 15), ('dave', 'B', 10), ('jane', 'B', 12)]
    
  </code>
</pre>
    
    
 sorted 는 Timesort 알고리즘을 사용하며 이 알고리즘은 데이터 셋에 존재하는 순서를 이용하는 이점을 갖고 있다.   


Ref. https://docs.python.org/3/howto/sorting.html     
     http://blog.weirdx.io/post/50236     
     https://medium.com/@fiv3star/python-sorted-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-timsort-dca0ec7a08be     
