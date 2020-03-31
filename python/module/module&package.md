모듈(module)과 패키지(package)에 대해서 확실히 알아보자.     
파이썬 소스코드(스크립트)를 작성할 때마다 매번 비슷한 클래스와 함수를 작성한다면 코드도 길어지고 중복되는 부분이 생긴다.    
이런 경우에는 공통되는 부분을 모듈과 패키지로 만들면 된다.   

   
## modules (모듈)    
다수의 함수/클래스들을 정의해둔 파이썬 **소스코드 파일(스크립트 파일)**.     
전역변수, 함수 등을 모아둔 파일.
   
소스코드 이기 때문에 views.py 파일에 Post_cbv 라는 클래스가 있고 다른 파일에서 이 클래스를 사용하고 싶다면.     
<pre>
  <code>
    from .views import Post_cbv
  </code>
</pre>
    
위와 같이 선언해주면 사용가능하며 여기서 **모듈은 views.py 파일이 해당**한다.     
파일명이 모듈명에 해당하게 된다.    
    
또 다른 예.     
<pre>
  <code>
    class Person:
      def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address
        
      def getting(self):
        print('안녕하세요. 저는 {0}입니다.'.format(self.name))
  </code>
</pre>
    
이제 person.py 모듈에 Person 클래스를 사용해보자.     
    
<pre>
  <code>
    import person 
    
    hansub = person.Person('한섭', 26, '서울시 도봉구')
    hansub.greeting()
    
  </code>
</pre>
    
    
모듈과 관련이 있는  *if __name__ == '__main__':* 도 확실히 알고 넘어가자.     
      
<pre>
  <code>
    if __name__ == '__main__":
      코드
  </code>
</pre>
    
사실 이 코드를 매번 사용하지만 용도에 대해서 자세히 알지는 못했다.    
    
hello.py 라는 파일이 있다고 하자.     
<pre>
  <code>
    print('hello 모듈 시작')    
    print('hello.py __name__:', __name__) # __name__ 변수 출력    
    print('hello 모듈 끝')     
  </code>
</pre>

그리고 같은 폴더내에 main.py 라는 파일을 저장하자.    

<pre>
  <code>
    import hello
    
    print('main.py __name__:', __name__) 
  </code>
</pre>
    
실행 결과     
<pre>
  hello 모듈 시작     
  hello.py __name__: hello    
  hello 모듈 끝      
  main.py __name__: __main__    
</pre>
    
main.py 파일을 실행해보면 hello.py 파일과 main.py 파일의 __name__ 변수 값이 출력된다.       

파이썬에서 import로 모듈을 가져오면 해당 스크립트 파일이 한번 실행된다.     
따라서 hello 모듈을 가져오면 hello.py 안의 코드가 실행된다.      
__name__ 변수로 hello와 __main__이 들어가있는걸 확인할 수 있다.      
    
하지만 hello.py 파일을 실행하면,      
실행 결과     
<pre>
  hello 모듈 시작     
  hello.py __name__: __main__     
  hello 모듈 끝    
</pre>
    
__name__ 변수에 'hello'가 아니라 '__main__' 이 들어간걸 확인할 수 있다.     
**결론** 어떤 스크립트 파일이든 파이썬 인터프리터가 최초로 실행한 스크립트 파일의 __name__에는 '__main__'이 들어간다.      
이는 프로그램의 시작점(entry point)을 확인하기 위해 if __name__ == '__main__': 을 사용한다는 것을 의미한다.      
**즉, 스크립트 파일이 메인 프로그램으로 사용될 때와 모듈로 사용될 떄를 구분하기 위한 용도이다.**
   
위의 코드에서 hello.py 파일에는 시작점인지 확인하는 if __name__ == '__main__': 이 없어서 모든 코드가 실행되었지만,    
if __name__ == '__main__': 의 밑에 코드가 있고 시작점이 아닐경우 밑의 코드는 실행되지 않는다.     
      
    

## package (패키지)    
여러 모듈을 묶어 놓은 것.       
모듈은 한개의 소스코드(스크립트) 파일이지만, 패키지는 폴더(디렉터리)로 구성되어 있다.     

ref. https://dojang.io/mod/page/view.php?id=2449
