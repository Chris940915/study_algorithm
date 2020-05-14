

enter = input()

priority = {'*':2, '/':2, '+':1, '-':1}
stack = []
result = ''

for e in '('+enter+')':
    if 'A' <= e <= 'Z':
        result += e
    elif e == '(':
        stack.append(e)
    elif e == ')':
        while 1:
            temp = stack.pop()
            if temp == '(':
                break
            result += temp
    else:
        while stack[-1] != '(' and priority[stack[-1]] < priority[e]:
            result += stack.pop()
        stack.append(e)
print(result)