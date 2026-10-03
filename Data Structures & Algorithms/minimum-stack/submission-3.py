class MinStack:

    def __init__(self):
        self.s1 = []
        self.min_stack = []
        
    def push(self, val: int) -> None:
        self.s1.append(val)
        if len(self.min_stack) == 0:
            self.min_stack.append(val)
        elif self.min_stack[-1]>=val: # needs to be ">=" here beacuse otherwise if we have repeating numbers , the min stack will pop one minimum and run into error
            self.min_stack.append(val)
        

    def pop(self) -> None:
        popped = self.s1.pop()
        if popped == self.min_stack[-1]:
            self.min_stack.pop()
        

    def top(self) -> int:
        return self.s1[-1]
        
    def getMin(self) -> int:
        return self.min_stack[-1]

    # in this approach we are not storing min values repeatedly
    # another approach would be to store pairs of values in min_stack where we store (min, number of times that min occured) and during pop if min is equal to value we decrement the number of occurences and when it become 0 we pop it off the stack.
        
