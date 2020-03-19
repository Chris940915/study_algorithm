from collections import deque
import sys

LIMIT = 100001
input_ = sys.stdin.readline

def bfs(n, k):
    queue = deque([n])

    visit[n] = 0

    while queue:
        x = queue.popleft()

        if x==k:
            return visit[x]

        for n_x in (x-1, x+1):
            if 0<=n_x<LIMIT:
                if visit[n_x] == LIMIT:
                    visit[n_x] = visit[x]+1
                    queue.append(n_x)
        n_x = x*2
        if 0<=n_x<LIMIT:
            if visit[n_x] == LIMIT:
                visit[n_x] = visit[x]
                queue.append(n_x)
            #이미 왔다갔을 경우, 곱셉은 카운트가 안늘어나기 때문에 대소비교하여 작은 값(최소 경로)를 할당.
            else:
                visit[n_x] = min(visit[x], visit[n_x])


if __name__ == "__main__":
    n, k = map(int, input_().split())
    
    #최단 경로 저장.
    visit = [LIMIT]*LIMIT
    answer = bfs(n, k)
    print(answer)