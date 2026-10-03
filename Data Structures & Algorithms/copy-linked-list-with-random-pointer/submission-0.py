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
        dummy = Node(0)
        newHead = dummy
        oldHead = head
        imap = {None:None}
        while head:
            node = Node(head.val)
            imap[head] = node
            newHead.next = node
            head = head.next
            newHead = newHead.next
        newHead = dummy.next
        while newHead:
            newHead.random = imap[oldHead.random]
            newHead = newHead.next
            oldHead = oldHead.next
        return dummy.next




        