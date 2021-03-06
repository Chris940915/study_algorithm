그래프의 탐색 알고리즘인 DFS와 BFS에 대하여 알아보자.   
   
그래프는 정점과 간선으로 이루어진 자료구조의 일종. G = (V, E)   
이진 탐색트리나 트리보다 **그래프**는 복잡하다.   
자식이 딸린 노드로 구성되는 점은 같지만, 트리와 달리 **한 노드에 부모가 여럿 있을 수 있어서 사이클이 만들어질 수 있다.**   
그리고 노드 자체가 아닌 노드 사이의 링크에도 값 또는 가중치가 있을 수 있다.    
   
#### 깊이 우선 탐색(DFS)의 특징.   
  - 스택으로 구현. (스택으로 preorder 종주 구현과 유사)     
  - 자기 자신을 호출하는 순환(재귀) 알고리즘의 성격을 지님.   
  - 이 알고리즘을 구현할 때 주의할 점은 그래프 탐색의 경우 어떤 노드를 방문했었는지 여부를 반드시 검색해야한다는 것.
   
**시간 복잡도**   
  - 인접 리스트로 표현된 그래프 : O(N+E)   
  - 인접 행렬로 표현된 그래프 : O(N^2)   

#### 너비 우선 탐색(BFS)의 특징.   
  - 방문한 노드들을 차례로 저장한 후 꺼내는 자료구조인 큐(Queue)로 구현(즉, 선입선출(FIFO) 원칙으로 탐색).    
  - 루트 노드(혹은 임의의 노드)에서 시작해서 인접한 노드를 먼저 탐색하는 방법.   
  - 너비 우선 탐색은 재귀적으로 동작하지 않는다.   
  - 이 알고리즘을 구현할 때 주의할 점은 그래프 탐색의 경우 어떤 노드를 방문했었는지 여부를 반드시 검색해야한다는 것.    
      
     
      
그래프 문제는 문제 상황을 그래프로 모델링한 후에 풀이에 들어간다.     
이때 모델링으로 그래프의 연결관계를 나타내는 두 가지 방식이 있다.        
      
1. 인접 행렬       
2. 인접 리스트      

* 인접 행렬     
   
   인접 행렬은 그래프의 연결 관계를 **이차원 배열**로 나타내는 방식.     
   장점은 구현이 쉽다.    
   또한, 노드 간의 연결을 확인하면 되기 때문에 O(1)이라는 시간 복잡도로 확인할 수 있다.
   
   하지만, 단점도 있다.     
   전체 노드의 개수를 V, 간선의 개수를 E라고 했을때, 노드 i에 연결된 모든 노드들에 방문해보고 싶은 경우 adj[i][1] 부터 adj[i][V]까지 모두 확인해야 하기 때문에 총 O(V)의 시간이 걸린다.      
   노드의 개수에 비해가 간선의 개수가 적은 그래프라면 특정 노드와 연견될 노드들이 몇번인지 확인하기 위하여 모든 노드들을 확인해봐야한다.      
   그리고 간선의 개수와 상관없이 무조건 V^2 의 공간을 사용해야 한다.
   
* 인접 리스트    

   인접 리스트는 각각의 정점에 대하여 인접한 정점들을 저장하는 방식.     
   장점은 연결된 정점을 찾는데 필요한 곳만 확인한다.     
   또한, 필요한 만큼의 공간만을 활용한다.     
   
   하지만, 특정 노드 x와 y의 연결 여부를 보려면 연결된 정점을 모두 봐야한다. 
   
