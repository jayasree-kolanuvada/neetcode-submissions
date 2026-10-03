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
        imap = collections.defaultdict(lambda:Node(0)) # we do lambda because defaultdict expects a function with no parameters and with Node we need to pass a value, so wrapping it in lambda makes it a function that does not require a parameter 
        imap[None] = None # without this, imap[None] would create a new node with value 0 for the end of the list
        curr = head
        while curr:
            imap[curr].val = curr.val # we are retrieving the copied node 
            imap[curr].next = imap[curr.next]# need to point to the copied nodes
            imap[curr].random = imap[curr.random]
            curr = curr.next
        return imap[head] # we need to return the copied head




        