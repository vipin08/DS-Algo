class StackNode:
    def __init__(self,data):
        self.next = None
        self.data = data



class Stack:
    def __init__(self):
        self.root = None


    def push(self, new_data):
        newStackN = StackNode(new_data)
        newStackN.next = self.root
        self.root = newStackN

    def pop(self):
        temp = self.root
        if temp is None:
            return False
        self.root = self.root.next
        return temp.data

    def treverse(self):
        temp = self.root
        while(temp is not None):
            print(temp.data)
            temp = temp.next


stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)

stack.treverse()
