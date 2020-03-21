## 문제

오늘은 스타트링크에 다니는 사람들이 모여서 축구를 해보려고 한다. 축구는 평일 오후에 하고 의무 참석도 아니다.   
축구를 하기 위해 모인 사람은 총 N명이고 신기하게도 N은 짝수이다. 이제 N/2명으로 이루어진 스타트 팀과 링크 팀으로 사람들을 나눠야 한다.   

BOJ를 운영하는 회사 답게 사람에게 번호를 1부터 N까지로 배정했고, 아래와 같은 능력치를 조사했다.   
능력치 Sij는 i번 사람과 j번 사람이 같은 팀에 속했을 때, 팀에 더해지는 능력치이다. 팀의 능력치는 팀에 속한 모든 쌍의 능력치 Sij의 합이다. 
Sij는 Sji와 다를 수도 있으며, i번 사람과 j번 사람이 같은 팀에 속했을 때, 팀에 더해지는 능력치는 Sij와 Sji이다.

축구를 재미있게 하기 위해서 스타트 팀의 능력치와 링크 팀의 능력치의 차이를 최소로 하려고 한다. 위의 예제와 같은 경우에는 1, 4번이 스타트 팀, 2, 3번 팀이 링크 팀에 속하면 스타트 팀의 능력치는 6, 링크 팀의 능력치는 6이 되어서 차이가 0이 되고 이 값이 최소이다.


-----------------------------------

## 풀이   
   
구현하는데 조금 귀찮았다. combination을 두번을 중첩되게 사용해야한다.   

미흡했던 점 2가지는 1) 팀을 반으로 가를때 어떤 연산을 이용할 것인가 와 2) itertools의 combination 사용 이다.   
   
1)의 문제는 set을 사용하면 해결되며 set은 &, - 의 연산이 사용 가능하다는 것을 꼭 명심하자.   
따라서 set(team)-set(start)를 이용하여 중복된 숫자를 제거할 수 있었다.   
   
2)는 시간초과와 관련된 문제로 파이썬에 대한 이해가 더 필요하다는 것을 증명했다.    

python Itertools의 combinations 함수의 코드는 다음과 같다.   

<pre>
  <code>
    def combinations(iterable, r):
    
      pool = tuple(iterable)
      n = len(pool)
      
      if r > n:
        return
      indices = range(r)
      yield tuple(pool[i] for i in indices)
      while True:
        for i in reversed(range(r)):
          if indices[i] != i+n-r:
            break
        else:
          return 
        indices[i] += 1
        for j in range(i+1, r):
          indices[j] = indices[j-1] + 1
        yield tuple(pool[i] for i in indices)
  </code>
</pre>

return 으로 반환하는 함수와 달리 yield로 반환하는 generator로 combinations 뿐만 아니라 itertools의 결과값은 generator 객체로 반환된다.   
따라서, **iterable**하게 사용할 수 있다. (모든 generator는 iterator 이다.)    
**그러므로 반환된 generator를 list에 담지않고 for문에 담아서 하나씩 가져다가 사용할 수 있다.**

