"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # manipulating pointers :- we could add the copied nodes right after the original nodes. and for random pointer we could just point it to the next node in the list. and then we need to separate the two lists 
        if not head: # for when list is empty
            return None

        curr = head
        while curr:
            node = Node(curr.val)
            temp = curr.next
            curr.next = node
            node.next = temp
            curr = temp
        prev, curr = head, head.next # we dont necessarily have to keep track of curr, can calculate by doing prev.next. helps us avoid the extra checks for if curr.next
        while prev:
            if prev.random:
                curr.random = prev.random.next
            else:
                curr.random = None
            prev = prev.next.next
            if curr.next:
                curr = curr.next.next
        l1 = head
        l2 = head.next

        while l1: # we need to restore the original list as well
            temp = l1.next
            l1.next = temp.next
            if temp.next:
                temp.next = temp.next.next
            l1 = l1.next
        return l2




        