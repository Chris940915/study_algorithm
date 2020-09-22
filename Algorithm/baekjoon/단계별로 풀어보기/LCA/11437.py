from collections import deque




def make_graph(v, raw_edges, root):

    edges = [[] for _ in range(v+1)]
    check = [False]*(v+1)
    depth, tree = [[0]*(v+1) for _ in range(2)]
    check[root] = True

    for edge in raw_edges:
        edges[edge[0]].append(edge[1])
        edges[edge[1]].append(edge[0])
    q = deque([root])
    while len(q):
        cur = q.popleft()
        
        for search in edges[cur]:

            if check[search]: continue
            depth[search] = depth[cur] + 1
            check[search] = True
            tree[search] = cur
            q.append(search)
        
    return tree, depth


def lca(tree, depth, u, v):

    if depth[u] < depth[v]:
        u, v = v, u
    
    while depth[u] != depth[v]:
        u = tree[u]
    
    while u != v:
        u = tree[u]
        v = tree[v]
    return v



n = int(input())
edges = [list(map(int, input().split())) for _ in range(n-1)]

tree, depth = make_graph(n, edges, 1)
m = int(input())
result = list()

for _ in range(m):
    a, b = map(int, input().split())
    result.append(lca(tree, depth, a, b))

for r in result:
    print(r)