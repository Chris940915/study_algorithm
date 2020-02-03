def quick_sort(n_list):

    len_ = len(n_list)

    if len_ <= 1:
        return n_list

    pivot = n_list[0]

    small_list = [ele for ele in n_list[1:] if ele < pivot]
    large_list = [ele for ele in n_list[1:] if ele > pivot]

    return  quick_sort(small_list) + [pivot] + quick_sort(large_list)



if __name__ == "__main__":
    n = int(input())
    n_list = list()

    for i in range(n):
        n_list.append(int(input()))
    
    solution = quick_sort(n_list)

    for i in solution:
        print(i)