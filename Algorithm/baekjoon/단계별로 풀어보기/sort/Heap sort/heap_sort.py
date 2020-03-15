def heapify(unsorted, index, heap_size):
    largest = index

    left_index = n*2 + 1
    right_index = n*2 + 2

    if left_index < heap_size and unsorted[largest] < unsorted[left_index] : 
        largest = left_index

    if right_index < heap_size and unsorted[largest] < unsorted[right_index] :
        largest = right_index

    if largest != index:
        unsorted[largest], unsorted[index] = unsorted[index], unsorted[largest]
        
        # 최대값과 swap 후, subtree의 hepitfy. 
        heapify(unsorted, largest, heap_size)


def heap_sort(unsorted):
    n = len(unsorted)

    # complete binary tree 맨 뒤에서부터 정렬.
    # build-max-heap
    # 서로 한번씩 비교. O(n).
    for i in range((n//2)-1, -1, -1):
        heapify(unsorted, i, n)
    
    
    for i in range(n-1, 0, -1):
        unsorted[0], unsorted[n-1] = unsorted[n-1], unsorted[0]
        heapify(unsorted, 0, i)
    return unsorted


