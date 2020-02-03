

[기초적인 연결리스트 연산](##기초적인-연결-리스트-연산)

[연결 리스트 문제](#연결-리스트-문제)
  
    
      
      

연결 리스트(linked list)는 사실 워낙 간단해 보이지만 동적인 데이터를 처리하는 것과 관련된 수많은 문제의 근간을 이루는 자료구조.

효율적인 리스트 종주(traversal), 리스트 정렬, 리스트 앞이나 뒤쪽 끝에서의 삭제 또는 삽입에 대한 문제는 기초적인 자료구조 개념을 테스트하기에 더할 나위 없이 좋다. 리스트를 완벽하게 구현하는데 보통 10분이 채 걸리지 않기 때문에 문제를 푸는 시간은 충분하며 대조적으로 해시 테이블처럼 복잡한 자료구조는 구현하는 데만 많은 인터뷰 대부분의 시간을 차지한다.


* 연결 리스트의 종류  
  연결리스트는 3가지 유형으로 단일 연결 리스트(Singly-linked list), 이중 연결 리스트(doubly-linked list), 원형 연결 리스트(circularly-linked     lisat)이 존재한다.

인터뷰어가 "연결 리스트"라고만 말한다면 보통 단일 연결 리스트를 뜻함. 
단일 연결 리스트는 각각 다음 원소를 가리키는 next 포인터 또는 레퍼런스(연결 링크)가 들어있는 데이터 원소들로 구성된다.
리스트의 마지막 원소에는 빈 링크 또는 널 링크가 들어간다. 

  <pre>
  C이나 C++에서는 원소의 next포인터와 그 원소에 들어갈 데이터가 다음 코드에 있는 것처럼 하나로 묶여 있다. 

  <code>
    typedef struct intElement {
      struct intElement *next;
      int data;
    }intElement;
  </code>
  next 포인터를 구조체나 클래스 맨 앞 쪽에 넣어두면 그 원소에 어떤 데이터가 들어가든 제대로 동작하는 포괄적인 리스트 처리 루틴을 더 쉽게 만들 수 있다는 장점이 있다.
  </pre>
  
어떤 언어를 쓰든 단일 연결 리스트를 구현할 때는 몇가지 주의해야 할 특별 케이스 및 함정이 도사리고 있다.  
단일 연결 리스트의 연결 링크는 다음 원소를 가리키는 포인터(또는 레퍼런스)만으로 구성되기 때문에 리스트를 한 방향으로만 종주할 수 있다.  
__따라서 리스트를 완전히 종주하려면 반드시 첫 번째 원소부터 시작해야한다.__  
그래서 연결 리스트라는 용어를 어떤 연결 리스트의 첫 번째 원소라는 뜻으로 쓰는 경우도 종종 있다.   
   
*인터뷰어가 어떤 함수에서 인자로 연결 리스트를 받는다고 말하면, 그 연결리스트의 첫 번째 원소에 대한 포인터/레퍼런스를 인자로 받아들인다는 뜻으로 이해하면 된다.*

## 기초적인 연결 리스트 연산  

### 헤드 원소 추적
단일 연결 리스트에서는 반드시 헤드 원소를 추적해야 한다.  

<pre>
따라서 새로운 원소를 첫 번째 원소 앞에 추가한다거나 첫 번째 원소를 제거할 때 리스트의 헤드에 대한 포인터 또는 레퍼런스를 갱신해야 한다.
<code>
  bool insertInFront(intElement *head, int data){
    intElement *newElem = new intElement;
    if (!newElem) return false;
    
    newElem->data = data;
    head = newElem; // 틀렸음.
    return true;
}

</code>

위 코드에서는 헤드 포인터에 대한 지역 변수 사본만을 갱신하기 때문에 이 코드는 제대로 작동하지 않는다. (함수 인자로 단일 포인터 사용.)   
제대로 작동하게 하려면 **헤드 포인터에 대한 포인터**를 넘겨줘야 한다.

<code>
  bool insertInFront(intElement **head, int data){
    intElement *newElem = new intElement;
    if (!newElem) return false;
    
    newElem->data = data;
    *head = newElem; // 더블 포인터를 사용하여 헤드의 주소를 갱신.
    return true;
}
</code>
</pre>

### 종주 

헤드 원소가 아닌 다른 리스트 원소를 가지고 작업을 해야하는 경우도 있다.  
연결 리스트의 첫 번째 원소가 아닌 원소에 대한 연산을 하려면 리스트에 있는 원소 중 일부를 종주해야 할 수도 있으며,   
   
*이때 항상 리스트가 끝나지 않는지 확인을 해야한다.*

<pre>
  아래에 있는 코드는 틀린 코드다. (java code)
<code>
  public intElement find(intElement head, Object data){
      while(head.data != data){
          head = head.next;
      }
      return head;
  }
</code>

리스트가 끝났는지 확인하기 위하여 head != null을 추가하여 리스트가 끝났는지 확인.

<code>
  public intElement find(intElement head, Object data){
    while(head != null && head.data != data){ 
        head = head.next;
    }
    return head;
  }
</code>
</pre>


### 원소의 삽입 및 삭제   

단일 연결 리스트에 있는 원소들은 다음 원소에 대한 링크를 통해서만 관리할 수 있기 때문에 중간에 있는 원소를 삽입 또는 삭제하려면, 그 앞 원소의 링크를 수정해야 한다.  
그리고 그 앞 원소를 알아낼 방법이 없기 때문에 **리스트를 종주해야 할 수 있다.**

<pre>
    리스트의 헤드 부분을 처리할 때는 한층 더 주의를 기울여야한다.
<code>
    bool deleteElement(intElement **head, intElement *deleteme){
      intElement *elem = *head;

      if (deleteme == *head) {
          *head = elem->next;
          delete deleteme;
          return true;
      }

      while(elem) {
          if(elem->next == deleteme){
              elem->next = deleteme->next;
              delete deleteme;
              return true;
          }
          elem = elem -> next;
      }
      // *deletme 가 없는 경우*
      return false;
  }
</code>

삭제 및 삽입을 하려면 삭제 및 삽입할 위치의 바로 앞에 있는 원소에 대한 포인터 or 레퍼런스가 필요.

</pre>

*한가지 더 신경 써야 할 문제.*    
   
연결 리스트에 있는 모든 원소를 삭제하고자 하는 경우.   
가장 쉽게 생각할 수 있는건 포인터 1개를 사용하여 리스트를 종주하면서 원소들을 하나씩 제거하는 방법.  
**BUT,** 실제로 구현하려고 하면 문제가 생김.   
다음 포인터로 넘어가는 작업과 원소를 제거하는 작업 중 어느 것을 먼저 해야할까?   
1. 다음 포인터로 넘어가는 일을 먼저 하면 제거해야할 원소의 포인터를 덮어쓴 상황이기 때문에 메모리 할당을 해제할 수가 없다.   
2. 제거를 먼저 해버리고 나면 방금 제거한 원소에 next 포인터가 사라져 다음 원소로 넘어가는 것이 불가능하다.   
     
<pre>
따라서, 다음 코드처럼 포인터를 2개 써야한다. 
<code>
    void deleteList(intElement **head){
      intElement *deleteme = *head;

      while(deleteme){
          intElement *next = deleteme->next;
          delete  deleteme;
          deleteme = next;
      }

      *head = NULL;
  }
</code>
</pre>

원소를 삭제할 때는 적어도 두 개의 포인터 변수가 필요.   
삽입할 때도 포인터 변수가 두 개 있어야 하는 것은 마찬가지지지만, 둘 중 하나는 리스트에 있는 원소를 위해 쓰이고, 다른 하나는 메모리 할당에 의해 반환되는 포인터용으로 쓰이기 때문에 삽입 연산에서 포인터를 한 개만 쓰는 실수를 범하는 일은 거의 없다. 


## 연결 리스트 문제
