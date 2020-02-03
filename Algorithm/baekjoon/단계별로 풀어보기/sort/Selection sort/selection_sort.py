def selection_sort(n_list):

    len_ = len(n_list)

    for i in range(len_):
        min_idx = i
        for j in range(i+1, len_):
            if n_list[min_idx] > n_list[j]:
                min_idx = j
        n_list[min_idx], n_list[i] = n_list[i], n_list[min_idx]

    return n_list




if __name__ == "__main__":
    n = int(input())
    n_list = list()

    for i in range(n):
        n_list.append(int(input()))

    solution = selection_sort(n_list)

    for i in solution:
        print(i)