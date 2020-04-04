파이썬은 추상 클래스(abstract class)라는 기능을 제공.    
**추상 클래스는 메서드의 목록만 가진 클래스로 상속받는 클래스에서 매서드 구현을 강제하기 위해 사용.**   
    
먼저 추상 클래스를 만들려면 import로 abc 모듈을 가져와야 한다. (abstact base class의 약자.)    
그리고 클래스의 ( ) (괄호)안에 *metaclass = ABCMeta*를 지정하고, 메서드를 만들 때 위에 @abstractmethod 를 붙여서 추상 메서드로 지정합니다.    
    
<pre>
  <code>
    from abc import *
    
    class 추상클래스이름(metaclass=ABCMeta):
      @abstractmethod
      def 메서드이름(self):
        코드
    
  </code>
</pre>
    
여기서 from abc import *로 abc 모듈의 모든 클래스와 메서드를 가져왔습니다.     
만약 *import abc*로 모듈을 가져왔다면 abc.ABCMeta, @abc.abstractmethod로 사용해야 한다.     
      
그럼 학생 추상 클래스 StudentBase를 만들고, 이 추상 클래스를 상속받아 학생 클래스 Student를 만들어보자.      

<pre>
  <code>
    from abc import *
    
    class StudentBase(metaclass=ABCMeta):
      @abstractmethod
      def study(self):
        pass
        
      @abstractmethod
      def go_to_school(self):
        pass
        
     class Student(StudentBase):
      def study(self):
        print('공부하기')
        
     james = Student()
     james.study()
   </code>
 </pre>
    
 위의 코드는 StudentBase 추상 클래스의 go_to_school 추상 메서드를 Student 클래스가 구현하지 않았기 때문에 오류가 발생한다.    
 **추상 클래스를 상속받았다면 *@abstractmethod*가 붙은 추상 메서드를 모두 구현해야 한다.   
 다음과 같이 Student에도 go_to_school 메서드도 구현해준다.    
    
 <pre>
  <code>
    from abc import *
 
class StudentBase(metaclass=ABCMeta):
    @abstractmethod
    def study(self):
        pass
 
    @abstractmethod
    def go_to_school(self):
        pass
 
    class Student(StudentBase):
        def study(self):
            print('공부하기')

        def go_to_school(self):
            print('학교가기')

    james = Student()
    james.study()
    james.go_to_school()
    </code>
    
    공부하기
    학교가기
</pre>

이처럼 추상 클래스는 파생 클래스가 반드시 구현해야 하는 메서드를 정해줄 수 있다.     
추상 클래스의 추상 메서드를 모두 구현했는지 확인하는 시점은 **파생 클래스가 인스턴스를 만들 때**이다.   
위의 코드에서는 james = Student()에서 확인한다.      
   
    
Ref. 
    https://dojang.io/mod/page/view.php?id=2389
