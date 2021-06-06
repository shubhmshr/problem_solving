'''
push(e)
pop
top
is_empty()
len()

'''

class ArrayStack:
    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def is_empty(self):
        return len(self._data) == 0

    def top(self):
        if self.is_empty():
            raise Exception("Stack is Empty")
        else:
            return self._data[-1]

    def pop(self):
        if self.is_empty():
            raise Exception("Cannot pop since stack is empty")
        else:
            return self._data.pop()

    def push(self, element):
        return self._data.append(element)


if __name__ == "__main__":
    stack = ArrayStack()
    print(stack.__len__())
    stack.push(4)
    print(stack.top())