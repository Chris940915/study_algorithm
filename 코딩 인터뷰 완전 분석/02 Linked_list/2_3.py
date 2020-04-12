class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

class Linked_List:

    def __init__(self):
        self.head = None
        self.tail = None
    
    # 처음에 예외처리를 잊지말자.
    # False 와 True는 연산이 성공적으로 되었냐 안되었냐를 나타내는 기본적인 기법.
    def del_node(self, node):
        if node is None or node.next is None:
            return False
        
        next_node = node.next

        node.data = next_node.data
        node.next = next_node.next

        return True
    
    # 이건 인자로 받은 노드를 삭제하는 함수가 아니라 
    # 인자로 받은 노드의 다음 노드를 삭제하기 때문에 답과 다르다..
    def del_node_2(self, node):
        if node is None or node.next is None:
            return False
        
        next_node = node.next
        node.next = next_node.next

        return True