def insertion_sort(n_list):
    len_ = len(n_list)

    for i in range(1, len_):      # i를 하나씩 원소가 들어온다고 생각. 
        for j in range(i, 0, -1): # j를 i(원소의 개수) 뒤에서 부터 하나씩 앞으로.
            if n_list[j-1] > n_list[j]:
                n_list[j-1], n_list[j] = n_list[j], n_list[j-1]

    return n_list



if __name__ == "__main__":
    n = int(input())
    n_list = list()

    for i in range(n):
        n_list.append(int(input()))

    solution = insertion_sort(n_list)

    for i in solution:
        print(i)