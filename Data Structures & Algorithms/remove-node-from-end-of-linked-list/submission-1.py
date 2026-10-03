# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head) # remeber for next time 
        slow, fast = dummy, head # slow = dummy allows us to account for the cases when list is short
        while n > 0:
            fast = fast.next
            n -= 1
        
        while fast: # here we allow fast to become null, since slow is already one step behind it lands on the node just before the node that needs to be deleted 
            slow = slow.next
            fast = fast.next
        
        #temp = slow.next.next
        #slow.next = temp -------> doesnt work for empty list / list too short edge cases a cleaner way to do it would be:- 

        slow.next = slow.next.next # beacuse we set slow to dummy let us say we have [5], slow would be set to 0 and we can easily set 0.next = 0.next.next which would be 0 -> None , correctly deleting 5
        return dummy.next


        

        
        