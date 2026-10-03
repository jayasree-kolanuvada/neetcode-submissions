class MyCircularQueue:

    def __init__(self, k: int):
        self.queue = [None]*k
        self.head = 0
        self.size = 0
        self.rear = -1
        self.k = k

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        self.rear = (self.rear + 1)%self.k
        self.queue[self.rear] = value
        self.size += 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.queue[self.head] = None
        self.head = (self.head + 1)%self.k
        self.size -= 1
        return True
        

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[self.head]
        

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[self.rear]
        

    def isEmpty(self) -> bool:
        if self.size == 0:
            return True
        return False
        

    def isFull(self) -> bool:
        if self.size == self.k:
            return True
        return False

# an array is better suited for this circular queue than a linked list or a dll because the size of the queue is prefixed and as a result we do no need to make new nodes and waste memory on pointers. the elements also sit next to each other in memory which suits the cpu cache and the empty slots can be reused since it is circular. A ll would be better suited when u have to resize the queue / size isnt mentioned 

# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()