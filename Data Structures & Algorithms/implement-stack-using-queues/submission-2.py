class MyStack:

    def __init__(self):
        self.q = None

    def push(self, x: int) -> None:
        self.q = deque([x, self.q])

    def pop(self) -> int:
        top = self.q.popleft()
        self.q = self.q.popleft()
        return top

    def top(self) -> int:
        return self.q[0]

    def empty(self) -> bool:
        return not self.q


# This builds the stack as a chain of nested two-element deques, like a linked list where each node is `deque([value, rest_of_stack])`.
# Push wraps the current stack inside a new deque, with the new value at the front:
#
# s.push(1)   # q = deque([1, None])
# s.push(2)   # q = deque([2, deque([1, None])])
# s.push(3)   # q = deque([3, deque([2, deque([1, None])])])
#
# So `q[0]` is always the most recently pushed value, the top of the stack, and `q[1]` is the entire stack beneath it.
# Pop unwraps one layer:
#
# top = self.q.popleft()      # takes 3; q is now deque([deque([2, ...])])
# self.q = self.q.popleft()   # takes the inner deque; q = deque([2, deque([1, None])])
# return top                  # 3
#
# The first `popleft` gets the value. The second gets the rest of the stack, which becomes the new `q`.
# Top reads `q[0]` without removing anything.
# Empty works because once everything has been popped, `q` ends up back at `None`, and `not None` is `True`. After popping the last element, `q` is `None`, so this check is reliable.
# Every operation is O(1), unlike the usual approach of rotating the whole queue on each push. It’s a clever trick: it only uses the queue operations allowed in the problem, `popleft` and building a deque, but treats each deque as a pair rather than as a real queue. It’s essentially a linked list built out of deques.