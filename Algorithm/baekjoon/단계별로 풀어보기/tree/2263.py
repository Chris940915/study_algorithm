

n = int(input())
in_order = list(map(int, input().split()))
post_order = list(map(int, input().split()))
in_location = [0 for _ in range(n+1)]
tree = [[0,0] for _ in range(n+1)]

for i in range(n):
    in_location[in_order[i]] = i

def find_tree(in_l, in_r, post_l, post_r):

    if post_l <= post_r:
        parents = post_order[post_r]
        p_index = in_location[parents]

        l_count = p_index - in_l
        if l_count > 0:
            tree[parents][0] = post_order[post_l+l_count-1]

        r_count = in_r - p_index
        if r_count > 0:
            tree[parents][1] = post_order[post_r-1]
        
        find_tree(in_l, p_index-1, post_l, post_l+l_count-1)
        find_tree(p_index+1, in_r, post_r-r_count ,post_r-1)



def pre_order(root):

    print(root, end=' ')

    if tree[root][0] != 0:
        pre_order(tree[root][0])
    
    if tree[root][1] != 0:
        pre_order(tree[root][1])
    
find_tree(0, n-1, 0, n-1)
pre_order(post_order[-1])

