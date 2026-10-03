class MinStack:

    def __init__(self):
        self.s1 = []
        self.min_stack = []
        
    def push(self, val: int) -> None:
        self.s1.append(val)
        if len(self.min_stack) == 0:
            self.min_stack.append(val)
        elif self.min_stack[-1]>=val:
            self.min_stack.append(val)
        

    def pop(self) -> None:
        popped = self.s1.pop()
        if popped == self.min_stack[-1]:
            self.min_stack.pop()
        

    def top(self) -> int:
        return self.s1[-1]
        
    def getMin(self) -> int:
        return self.min_stack[-1]
        
