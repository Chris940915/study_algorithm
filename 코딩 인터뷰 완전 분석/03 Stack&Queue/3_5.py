'''
    큐와 스택의 주된 차이는 순서.

    두 번째 스택을 사용해서 뒤집기 + lazy 접근법

'''

class Stack:
    def __init__(self):
        self.list = []
    
    def pop(self):
        data = self.list.pop()
        return data
    
    def push(self, data):
        self.list.append(data)
    
    def peek(self):
        return self.list[-1]

    def size(self):
        return len(self.list)

    def is_empty(self):
        if self.size() == 0:
            return True
        else:
            return False

class MyQueue:

    def __init__(self):
        self.new_stack = Stack()
        self.old_stack = Stack()

    def size(self):
        return self.new_stack.size() + self.old_stack.size()
    
    def add(self, data):
        self.new_stack.push(data)
    
    def shiftStack(self):
        if self.old_stack.is_empty():
            while not self.new_stack.is_empty():
                self.old_stack.push(self.new_stack.pop())

    def peek(self):
        self.shiftStack()
        return self.old_stack.peek()
    
    def remove(self):
        self.shiftStack()
        self.old_stack.pop()

