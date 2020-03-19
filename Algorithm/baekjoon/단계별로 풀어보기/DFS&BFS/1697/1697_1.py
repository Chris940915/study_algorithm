
# -1, 1, *2 3가지를 brute force로 탐색. 
#  동생 위치에 수빈이가 도달하면 종료. 
#  count 개수들을 리스트화 해서 가장 낮은 count를 리턴. 
#
#   필요한 변수 : count(초 세는것), count 를 담을 리스트. 
#   -1, 1, *2 를 리스트에 담아서 for i in range(3)로 표현?
#   계산 3가지 범위는 0<= <=100,000 이용.
#   


## 시간 초과난당...... 
from collections import deque
import sys

input_ = sys.stdin.readline
LIMIT = 100001

def bfs(n, k):
    queue = deque([n])
    count = 0
    candidate = 0

    if n==k:
        return count, candidate

    while not candidate:
        count += 1

        for _ in range(len(queue)):
            x = queue.popleft()

            for j in (x-1, x+1, x*2):
                if 0<=j<LIMIT:
                    if j==k:
                        candidate += 1
                    else:
                        queue.append(j)
    return count, candidate


n, k = map(int, input().split())
answer = bfs(n, k)
print(answer[0])
