class MinStack:

    def __init__(self):
        self.minStack = []
        self.mini = float("inf")
        
    def push(self, val: int) -> None:
        if self.minStack:
            mini = min(self.minStack[-1][1],val)
        else:
            mini = val
        self.minStack.append([val,mini])

    def pop(self) -> None:
        self.minStack.pop()
        
    def top(self) -> int:
        return self.minStack[-1][0]

    def getMin(self) -> int:
        return self.minStack[-1][1]
        
