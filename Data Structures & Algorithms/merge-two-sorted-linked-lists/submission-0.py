# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        elif not list2:
            return list1
        p1 = list1
        p2 = list2

        if p1.val <= p2.val:
            ans = ListNode(p1.val) 
            head = ans
            p1 = p1.next
        else:
            ans = ListNode(p2.val)
            head = ans
            p2 = p2.next

        while p1 or p2:
            if p1 != None and p2!= None:
                if p1.val <= p2.val:
                    ans.next = ListNode(p1.val)
                    ans = ans.next
                    p1 = p1.next
                else:
                    ans.next = ListNode(p2.val)
                    ans = ans.next
                    p2 = p2.next
            elif p1 != None:
                ans.next = ListNode(p1.val)
                ans = ans.next
                p1 = p1.next
            else:
                ans.next = ListNode(p2.val)
                ans = ans.next
                p2 = p2.next
        return head


        
        