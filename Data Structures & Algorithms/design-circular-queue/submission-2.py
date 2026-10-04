class ListNode:
    def __init__(self,val,nxt = None):
        self.val = val
        self.next = nxt

class MyCircularQueue:

    def __init__(self, k: int):
        self.k = k
        self.head = ListNode(0)
        self.tail = self.head

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        node = ListNode(value)
        if self.isEmpty():
            self.head.next = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.k-=1
        return True
        

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.head.next = self.head.next.next
        if not self.head.next:
            self.tail = self.head
        self.k+=1
        return True
        
    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.head.next.val
        

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.tail.val
        

    def isEmpty(self) -> bool:
        return self.head.next is None
        

    def isFull(self) -> bool:
        return self.k == 0
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()