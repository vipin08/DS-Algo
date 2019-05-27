class Queue:
    def __init__(self,capacity):
        self.front = self.size = 0
        self.rear = capacity - 1
        self.Q = [None]*capacity
        self.capacity = capacity

    def isFull(self):
        return self.size == self.capacity

    def isEmpy(self):
        return self.size == 0

    def EnQueue(self,item):
        if self.isFull():
            print("full")
            return
        self.rear = (self.rear + 1) % (self.capacity)
        self.Q[self.rear] = item
        self.size = self.size + 1
        print("%s enqueue t oqueue" %str(item))

    def DeQueue(self):
        if self.isEmpy():
            print("Empty")
            return

        print("%s dequqe from queue" % str(self.Q[self.front]))
        self.front = (self.front + 1) % (self.capacity)
        self.size = self.size -1



queue = Queue(30)
queue.EnQueue(10)
queue.EnQueue(20)
queue.EnQueue(30)

queue.DeQueue()
