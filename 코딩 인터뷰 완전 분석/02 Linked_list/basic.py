class Node:

    def __init__(self, data):
        self.data = data
        self.next = None
    

class Linked_list:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    
    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    
    def is_empty(self):
        if self.head:
            return False
        else:
            return True

    def pop(self):
        if is_empty():
            return -1
        
        data = self.head.data
        self.head = self.head.next

        return data

    
    def traverse(self):
        cur = self.head
        value_list = []

        while cur:
            value_list.append(cur.data)
            cur = cur.next
        return value_list
    
    def delete_duplicate(self):
        cur = self.head
        hash_table = dict()

        while cur:
            if cur.data not in hash_table:
                hash_table[cur.data] = 1
            else:
                cur.next = cur.next.next
            cur = cur.next
        
