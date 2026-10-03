class StockSpanner:

    def __init__(self):
        self.stack = [] # pair of (price, span)
        # here saving pairs of price and index will not work because the size of stack is constantly changing and price is int not list.
        

    def next(self, price: int) -> int:
        span = 1
        while self.stack and price >= self.stack[-1][0]:
            span += self.stack[-1][1]
            self.stack.pop()
        self.stack.append((price,span))
        return span
            
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)