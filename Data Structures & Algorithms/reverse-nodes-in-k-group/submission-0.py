# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        prev = dummy = ListNode()
        dummy.next = head
        while True:
            grp = k
            newTail = curr = head
            if not head:
                return dummy.next
            while grp > 1 and curr.next:
                curr = curr.next
                grp -= 1
            if grp > 1:
                return dummy.next
            head = curr.next
            curr.next = None
            newHead = self.reverse(newTail)
            prev.next = newHead
            newTail.next = head
            prev = newTail
                



    def reverse(self, node): # returns new head(Prev) of the reversed list
        head = node
        prev, curr = None, head
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev

        
        