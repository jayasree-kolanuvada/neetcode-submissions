class FreqStack:

    def __init__(self):
        self.maxstack = [[]]
        self.freq = dict()
        
    def push(self, val: int) -> None:
        f = self.freq.get(val,0) + 1
        self.freq[val] = f
        if f == len(self.maxstack):
            self.maxstack.append([])
        self.maxstack[f].append(val)
        

    def pop(self) -> int:
        ans = self.maxstack[-1].pop()
        self.freq[ans] -= 1
        if not self.maxstack[-1]:
            self.maxstack.pop()
        return ans
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()