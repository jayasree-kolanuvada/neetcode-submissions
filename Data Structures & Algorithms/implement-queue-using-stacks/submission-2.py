class MyQueue:

    def __init__(self):
        self.s1 = []
        self.s2 = []
    def push(self, x: int) -> None:
        while self.s1:
            self.s2.append(self.s1.pop())
        self.s1.append(x)
        while self.s2:
            self.s1.append(self.s2.pop()) 
        # we need to empty s1 first, then append the new ele into s1 cuz it need to go last and then transfer all elements from s2 into s1 to get them back to their original order. different from how stack is implemented usinQ where we have to rotate the list on every turn and swap the lists 
        

    def pop(self) -> int:
        if len(self.s1) == 0:
            return "Empty"
        return self.s1.pop()
        

    def peek(self) -> int:
        return self.s1[-1]
        

    def empty(self) -> bool:
        return len(self.s1)==0
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()