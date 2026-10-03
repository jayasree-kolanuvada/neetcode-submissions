class FreqStack:

    def __init__(self):
        self.freqmap = dict()
        self.maxstack = [[]] # pair of (val,freq)

    def push(self, val: int) -> None:
        freq = self.freqmap.get(val,0)+1
        self.freqmap[val] = freq
        if freq == len(self.maxstack):
            self.maxstack.append([])
        self.maxstack[freq].append(val)
        
    def pop(self) -> int:
        res = self.maxstack[-1].pop()
        self.freqmap[res]-=1
        if not self.maxstack[-1]:
            self.maxstack.pop()
        return res
        

        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()