class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class Linked_List:

    def __init__(self):
        self.head = None
        self.tail = None
    
    def check_palindrome(node):
        if node is None:
            return False

        reversed_list = revese(node)
        result = is_equal(node, reversed_list)

    def reverse(node):
        head = None

        while node != None:
            temp = head
            head = node
            head.next = temp
            node = node.next
        return head

    def is_equal(node_1, node_2):
        if node_1 == None or node_2 == None:
            return False
        
        while node_1 != None and node_2 != None:
            if node_1.data != node_2.data:
                return False

            node_1 = node_1.next
            node_2 = node_2.next
        return True
