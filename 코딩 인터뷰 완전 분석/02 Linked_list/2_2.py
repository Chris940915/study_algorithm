class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Linked_list:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def find_k(self):
        curr = self.head

        k_curr = self.head

        for _ in range(6):
            if k_curr == None:
                return None
            k_curr = k_curr.next
        
        while k_curr is not None:
            k_curr = k_curr.next
            curr = curr.next

        return curr.data
        