'''

두 가지 방법이 존재.

1. 각 상태마다 최솟값을 기록.
    최상위 노드(원소)만을보고 최솟값을 알아낼 수 있다.
    각 원소마다 최솟값을 기록. 
    스택이 커지면, 각 원소마다 min을 기록하느라 공간이 낭비된다.

2. min 값들을 기록하는 스택을 하나 더 두는 방법.
    만약 스택의 크기가 크긴 하지만 첫번째 원소가 최솟값이라면 하나의 원소만으로 찾을 수 있다.
'''

import sys

class Stack():
    def __init__(self):
        self.list = []
    
    def push(self, data):
        self.list.append(data)

    def pop(self):
        if not self.list:
            return False
        
        return self.list.pop()

    def peek(self):
        if not self.list:
            return False

        return self.list[-1]

    def is_Empty(self):
        if len(self.list) == 0:
            return True
        else:
            return False
            
class StackWithMin2(Stack):
    def __init__(self):
        self.s2 = Stack()
        
    def push(self, data):
        if data <= self.min():
            s2.push(data)
        super.push(data)
    
    def min(self):
        if s2.is_Empty():
            return sys.maxsize
        else:
            return s2.peek()
    
    def pop(self):
        value = super.pop()
        if (value == min()):
            s2.pop()
        return value