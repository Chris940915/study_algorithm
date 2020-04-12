class Node:

    def __init__(self, data):
        self.data = data
        self.next = None
    

class Linked_List:

    def __init__(self):
        self.head = None
        self.tail = None
    
    def setNext(self, node):
        curr = self.head
        next_ = Node()

        while curr.next is not None:
            curr = curr.next
        
        next_ = curr.next

        next_.data = node.data
        next_.next = curr.next.next


    def sum_list(node_1, node_2, next_v):
        if node_1 is None and node_2 is None and value is None:
            return None
        
        result = Node()

        value = next_v

        if node_1 != None:
            value += node_1.data
        
        if node_2 != None:
            value += node_2.data
        
        result.data = value%10

        if node_1 is not None or node_2 is not None:
            new_node = sum_list(node_1.next if node_1 is not None else None, node_2.next if node_2 is not None else None, 1 if value > 9: else 0)
            result.setNext(new_node)

        return result


