import sys
from collections import deque

LIMIT = 100001
input_ = sys.stdin.readline

def bfs(n, k, visit):
    queue = deque([n])

    while queue:
        x = queue.popleft()

        if x == k:
            return visit[x]

        for after_x in (x-1, x+1, x*2):
            if 0<=after_x<LIMIT:
                if not visit[after_x]:
                    # count를 따로 세지않고 이전 값에 +1 을 해주는 코딩방식이 시간 측면에서 더 좋다. 
                    # count를 세기 위하여 for 문을 단계마다 queue의 길이만큼 돌아야 하기떄문에. 
                    visit[after_x] = visit[x]+1
                    queue.append(after_x)
    

if __name__ == "__main__":
    n, k = map(int, input_().split())
    visit = [0]*LIMIT
    
    answer = bfs(n, k, visit)
    print(answer)
    