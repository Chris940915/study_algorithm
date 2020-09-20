

def make_tree(in_l, in_r, pre_l, pre_r):
    
    if pre_l <= pre_r:
        parents = preorder[pre_l]
        p_index = inorder.index(parents)

        l_count = p_index-in_l
        if l_count > 0:
            tree[parents][0] = preorder[pre_l+1]

        r_count = in_r-p_index
        if r_count > 0:
            tree[parents][1] = preorder[pre_r-r_count+1]
        
        # divide left subtree
        make_tree(in_l, p_index-1, pre_l+1, pre_l+l_count)

        # divide right subtree
        make_tree(p_index+1, in_r, pre_r-r_count+1, pre_r)


def postorder(node : int):

    if tree[node][0] != 0:
        postorder(tree[node][0])
    
    if tree[node][1] != 0:
        postorder(tree[node][1])
    
    result.append(node)


T = int(input())
for _ in range(T):
    n = int(input())
    preorder = list(map(int, input().split()))
    inorder = list(map(int, input().split()))
    tree = [[0, 0] for _ in range(n+1)]
    result = list()

    make_tree(0, n-1, 0, n-1)
    postorder(preorder[0])
    print(*result)