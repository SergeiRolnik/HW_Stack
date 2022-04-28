class Stack:

    def __init__(self):
        self.stack = []

    def isEmpty(self):
        return len(self.stack) == 0

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if self.isEmpty():
            return None
        else:
            return self.stack.pop()

    def peek(self):
        return self.stack[-1]

    def size(self):
        return len(self.stack)

open_brackets = ["[", "{", "("]
close_brackets = ["]", "}", ")"]

def check_balance(str):

    s = Stack()
    for bracket in str:
        if bracket in open_brackets:
            s.push(bracket)
        elif bracket in close_brackets:
            if not s.isEmpty() and open_brackets[close_brackets.index(bracket)] == s.peek():
                s.pop()
            else:
                return 'Unbalanced'

    if s.isEmpty():
        return 'Balanced'
    else:
        return 'Unbalanced'

strings = ['(((([{}]))))', '[([])((([[[]]])))]{()}', '{{[()]}}', '}{}', '{{[(])]}}', '[[{())}]', '(({{']

for str in strings:
    print(str, check_balance(str))