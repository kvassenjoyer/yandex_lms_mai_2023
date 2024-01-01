class Stack:
    # Стек
    
    stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        return self.stack.pop(-1)

    def is_empty(self):
        return not len(self.stack)
