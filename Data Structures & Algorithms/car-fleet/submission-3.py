class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [(p, s) for p, s in zip(position, speed)] 
        pair.sort(reverse=True)
        stack = []
        for p, s in pair:  # Reverse Sorted Order
            stack.append((target - p) / s)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop() # here we use if and not while because a car can only ever catch up to the car in front of it. no overtaking allowed.
        return len(stack)

        # you know logic but this is to improve python programming. like zip, inner loop