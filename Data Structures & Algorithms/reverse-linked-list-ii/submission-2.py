# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        l = r = dummy
        while left > 1:
            l = l.next
            left-=1
            right-=1
        prev, curr = None, l.next
        while right > 0:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
            right-=1
        l.next.next = curr
        l.next = prev
        if l==dummy:
            return l.next
        return head
        