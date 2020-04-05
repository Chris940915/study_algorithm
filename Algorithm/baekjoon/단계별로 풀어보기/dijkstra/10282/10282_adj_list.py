import sys
input = sys.stdin.readline

INF = sys.maxsize

def solution(k, s, graph):
    visit = [False] * k
    distance = [INF] * k
    distance[s] = 0
    
    while True:
        n = -1
        m = INF

        for j in range(k):
            if not visit[j] and m > distance[j]:
                m = distance[j]
                n = j
        if m == INF:
            break

        visit[n] = True

        if not matrix[n]:
            continue

        for m in matrix[n]:
            via = distance[n] + m[1]
            if distance[m[0]] > via:
                distance[m[0]] = via       
 
    return distance


T = int(input())

for _ in range(T):
    n, d, c = map(int, input().split())
    
    matrix = [[] for _ in range(n)]

    for _ in range(d):
        a, b, s = map(int, input().split())
        matrix[b-1].append([a-1,s])
        

    count = 0
    max_V = -(sys.maxsize-1)

    for i, mat in enumerate(matrix):
        result = solution(n, i, matrix)
        for m in mat:
            count += 1
            max_V = max(max_V, result[m[0]])
 
    print(count, max_V)


