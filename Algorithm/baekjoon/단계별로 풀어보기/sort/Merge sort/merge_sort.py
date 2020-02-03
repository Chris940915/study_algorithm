
def merge_sort(n_list):

    if len(n_list) <= 1:
        return n_list

    m = len(n_list) // 2
    
    left_ = n_list[:m]
    right_ = n_list[m:]
    
    left_update = merge_sort(left_)
    right_update = merge_sort(right_)

    return merge(left_update, right_update)

def merge(left_list, right_list):
    i = 0
    j = 0
    final = list()

    while i < len(left_list) and j < len(right_list) :
        if left_list[i] > right_list[j]:
            final.append(right_list[j])
            j += 1
        else:
            final.append(left_list[i])
            i += 1
    
    while i < len(left_list):
        final.append(left_list[i])
        i += 1
    
    while j < len(right_list):
        final.append(right_list[j])
        j += 1
    
    return final

if __name__ == "__main__":
    
    n = int(input())
    n_list = list()

    for i in range(n):
        n_list.append(int(input()))
    
    solution = merge_sort(n_list)
    
    for i in solution:
        print(i)