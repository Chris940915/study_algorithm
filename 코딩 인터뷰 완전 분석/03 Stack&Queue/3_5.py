class Stack:

    def __init__(self):
        self.list = []

    def push(self, data):
        self.list.append(data)
    
    def pop(self):
        return self.list.pop()
    
    def peek(self):
        return self.list[-1]
    
    def size(self):
        return len(self.list)

    def is_empty(self):
        if self.size() == 0:
            return True
        else:
            return False

def sort_stack(stack_s):
    stack_r = Stack()

    while not stack_s.is_empty():
        tmp = stack_s.pop()

        while stack_r.is_empty() or tmp < stack_r.peek():
            stack_s.push(stack_r.pop())
        stack_r.push(tmp)

    while not stack_r.is_empty():
        stack_s.push(stack_r.pop())