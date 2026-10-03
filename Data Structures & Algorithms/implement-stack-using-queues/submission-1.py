from collections import deque

class MyStack:
    def __init__(self):
        self.queue = deque()

    def push(self, x: int) -> None:
        self.queue.append(x)
        # rotate the queue so the just-pushed element moves to the front
        for _ in range(len(self.queue) - 1):
            self.queue.append(self.queue.popleft())

    def pop(self) -> int:
        return self.queue.popleft()

    def top(self) -> int:
        return self.queue[0]

    def empty(self) -> bool:
        return len(self.queue) == 0
        
#a regular Python list is backed by a contiguous array, so adding/removing from the end is O(1), but adding/removing from the front (insert(0, x) or pop(0)) is O(n) — every other element has to shift over to fill the gap or make room. deque is implemented as a doubly-linked list of blocks internally, so both ends are O(1) — that's the entire point of it.

#d = deque([1, 2, 3])
#d.append(4)        # add to right: deque([1, 2, 3, 4])
#d.appendleft(0)     # add to left: deque([0, 1, 2, 3, 4])
#d.pop()             # remove from right, returns 4: deque([0, 1, 2, 3])
#d.popleft()         # remove from left, returns 0: deque([1, 2, 3])


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()