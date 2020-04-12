
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None    

    # 임시 버퍼 사용.
    def del_duplicate_1(self):
        dict_ = dict()

        curr = self.head
        dict_[curr.data] = 1
        
        while curr.next is not None:
            if curr.next.data in dict_:
                curr.next = curr.next.next
            else:
                dict_[curr.next.data] = 1
            curr = curr.next
    
    # 임시 버퍼 없이 구현.
    def del_duplicate_2(self):
        curr = self.head

        while curr.next is not None:
            check = curr

            while check.next is not None:
                if curr.data == check.next.data:
                    check.next = check.next.next
            curr = curr.next