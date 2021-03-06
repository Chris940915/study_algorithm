
## 문제 

수빈이는 동생과 숨바꼭질을 하고 있다. 수빈이는 현재 점 N(0 ≤ N ≤ 100,000)에 있고, 동생은 점 K(0 ≤ K ≤ 100,000)에 있다.    
수빈이는 걷거나 순간이동을 할 수 있다. 만약, 수빈이의 위치가 X일 때 걷는다면 1초 후에 X-1 또는 X+1로 이동하게 된다.    
순간이동을 하는 경우에는 1초 후에 2*X의 위치로 이동하게 된다.

수빈이와 동생의 위치가 주어졌을 때, 수빈이가 동생을 찾을 수 있는 가장 빠른 시간이 몇 초 후인지 구하는 프로그램을 작성하시오

-------------------------------------

## 풀이   
   
아직 실력이 부족해서 풀긴 했지만 시간초과와 메모리 초과를 겪어 맞추진 못했다.   
구글에 많은 멋진 분들이 답을 알려준걸 참고해 내 식대로 다시 코딩해봤다.   

처음에 초과를 겪은 나의 코드는 queue에 새로운 원소들을 담고 queue의 길이만큼 for문을 돌려서 단계별로 진행하는 방식이다.   
하지만, for문을 queue의 길이만큼 돌려야 해서 문제가 생겼다.   
이 문제를 다른 분들께서는 최단 거리의 길이를 담는 배열을 선언하여 해결하였다.   
그래서 for문에 이동 원소들의 최단 거리가 없을때 값을 채워넣고 그 이동 원소를 큐에 담았다.
   
base는 queue에서 원소를 하나씩 뺄때, 그 원소가 목적지와 동일하면 리턴하게 만들었다.

#### 알게된 점.
   

그래프가 아니라 다른 알고리즘에서도 이전 값을 참조할때 어떻게 해야하는지. 
1초 후에 이동할때, x-1, x+1, x*2를 리스트나 튜플에 넣고 for문을 돌리는 코딩 방식을 몰랐다.
최단 거리의 길이를 담는 배열을 선언할때 값을 0으로 선언하면 오류가 발생.
