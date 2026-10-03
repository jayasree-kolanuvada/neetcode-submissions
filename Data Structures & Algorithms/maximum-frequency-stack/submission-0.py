class FreqStack:

    def __init__(self):
        self.freqmap = dict()
        self.maxstack = [] # pair of (val,freq)

    def push(self, val: int) -> None:
        temp = []
        self.freqmap[val] = self.freqmap.get(val,0)+1
        freq = self.freqmap[val]
        while self.maxstack and freq<self.maxstack[-1][1]:
            temp.append(self.maxstack.pop())
        self.maxstack.append((val,freq))
        for i in range (len(temp)-1,-1,-1):
            self.maxstack.append(temp[i])

    def pop(self) -> int:
        tempv = self.maxstack[-1][0]
        self.freqmap[tempv]-=1
        self.maxstack.pop()
        return tempv

        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()