import sys
import heapq

INF = sys.maxsize


def dijkstra(n, v, graph):

    distance = [INF]*n
    distance[v] = 0
    q = []    
    heapq.heappush(q, [0, v])

    while q:
        c, p = heapq.heappop(q)
        for pos, cost in graph[p]:
            cost += c

            if cost < distance[pos]:
                distance[pos] = cost
                heapq.heappush(q, [cost, pos])
    return distance

if __name__ == "__main__":
    

    v, e = map(int, input().split())
    s = int(input())
    matrix = [[] for _ in range(v)]
    for _ in range(e):
        a, b, c = map(int, input().split())
        matrix[a-1].append([b-1, c])
    answer = dijkstra(v, s-1, matrix)

    for a in answer:
        if a == INF:
            print("INF")
        else:
            print(a)
