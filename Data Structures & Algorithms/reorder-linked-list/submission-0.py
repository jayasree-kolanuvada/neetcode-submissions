# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # we first try to find the middle of the ll , then starting from the middle reverse the list and then try to join the respctive nodes with eachother 
        # to Find the middle of a linked list we use the two pointer method. we move the slow pointer once and the fast pointer twice. whenever the fast pointer reaches null it means that the slow pointer is at the middle of the list 

        slow, fast = head,head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        mid = slow.next
        slow.next = None
        prev = None

        while mid:
            temp = mid.next
            mid.next = prev
            prev = mid
            #if temp == None:
                #break.  ----> this can be handled in a better way by just setting mid = prev later
            mid = temp

        #node = head
        #head = head.next
        #count = 1
        #while mid or head:
            #count+=1
            #if mid and count%2 == 0:
                #node.next = mid
                #mid = mid.next
            #elif head:
                #node.next = head
                #head = head.next
            #node = node.next

    # The entire above chunk of code can be written in a cleaner way by taking a node from the first half, then from the second half and continue till the second half is exhausted 

        first, mid = head, prev
        while mid:
            temp1, temp2 = first.next, mid.next
            first.next = mid
            mid.next = temp1
            first, mid = temp1, temp2
            


        #0 -> 1 -> 2 -> 3 -> 4