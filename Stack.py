class StackNode:
    def __init__(self,data):
        self.head = None
        self.data = data


class Stack:
    def __init__(self):
        self.root = None

    def isEmpty(self):
        return True if self.root is None else False

    def push(self, data):
        new_data = StackNode(data)
        new_data.next  = self.root
        self.root = new_data

    def pop(self):
        if(self.isEmpty()):
            return float("-inf")
        temp = self.root
        self.root= self.root.next
        poppd = temp.data
        return poppd

    def peek(self):
        if self.isEmpty():
            return float("-inf")
        return self.root.data

stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)


print(stack.pop())
print(stack.peek())
