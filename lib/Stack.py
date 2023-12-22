class Stack:

    def __init__(self, items=[], limit=100):
        self.items = items
        self.limit = limit

    def isEmpty(self):
        return not bool(self.items)

    def push(self, item):
        if len(self.items) < self.limit:
            self.items.append(item)

    def pop(self):
        try:
            if self.isEmpty():
                raise IndexError("Stack is empty")
            return self.items.pop()
        except IndexError as e:
            return None

    def peek(self):
        if self.isEmpty():
            raise IndexError("Stack is empty")
        return self.items[-1]

    def size(self):
        return len(self.items)

    def full(self):
        return len(self.items) >= self.limit

    def search(self, target):
        for i in range(len(self.items) - 1, -1, -1):
            if self.items[i] == target:
                return len(self.items) - i - 1
        return -1
