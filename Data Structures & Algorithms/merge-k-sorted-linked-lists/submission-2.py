# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(
        self, lists: List[Optional[ListNode]]
    ) -> Optional[ListNode]:
        amount = len(lists)
        interval = 1
        while interval < amount:
            for i in range(0, amount - interval, interval * 2):
                lists[i] = self.merge2Lists(lists[i], lists[i + interval])
            interval *= 2

        return lists[0] if amount > 0 else None

    def merge2Lists(self, l1, l2):
        head = point = ListNode(0)
        while l1 and l2:
            if l1.val <= l2.val:
                point.next = l1
                l1 = l1.next
            else:
                point.next = l2
                l2 = l1
                l1 = point.next.next
            point = point.next

        if not l1:
            point.next = l2
        else:
            point.next = l1

        return head.next

'''Start with 5 lists at indices 0 to 4:

index:   0    1    2    3    4
       [L0] [L1] [L2] [L3] [L4]

interval is the distance between the two lists being merged in a round.

Round 1: interval = 1
python
range(0, 5 - 1, 2)  →  range(0, 4, 2)  →  i = 0, 2
i	merges	result stored in
0	lists[0] + lists[1]	lists[0] = L0+L1
2	lists[2] + lists[3]	lists[2] = L2+L3
index:   0       1    2       3    4
       [L0+L1]  ·   [L2+L3]  ·   [L4]

· marks a slot that has already been merged into another one. Its value is ignored from now on. L4 has no partner this round, so it just waits.

interval *= 2 gives 2.

Round 2: interval = 2
python
range(0, 5 - 2, 4)  →  range(0, 3, 4)  →  i = 0
i	merges	result stored in
0	lists[0] + lists[2]	lists[0] = L0+L1+L2+L3

i = 4 isn't in the range (it's ≥ 3), so L4 waits again.

index:   0              1    2    3    4
       [L0+L1+L2+L3]   ·    ·    ·   [L4]

interval *= 2 gives 4.

Round 3: interval = 4
python
range(0, 5 - 4, 8)  →  range(0, 1, 8)  →  i = 0
i	merges	result stored in
0	lists[0] + lists[4]	lists[0] = everything
index:   0                 1    2    3    4
       [L0+L1+L2+L3+L4]   ·    ·    ·    ·

interval *= 2 gives 8.

Stop: interval = 8

8 < 5 is false, so the loop ends. The answer is in lists[0].

The full picture
Round 1 (interval 1):   L0  L1  L2  L3  L4
                         \  /    \  /    |
Round 2 (interval 2):    [01]    [23]    |
                            \    /       |
Round 3 (interval 4):       [0123]       |
                                \       /
                               [01234]
Why the loop bounds work
Step interval * 2: at the start of each round, the "live" lists sit at indices that are multiples of interval (round 1: 0,1,2,3,4; round 2: 0,2,4; round 3: 0,4). Stepping by 2 * interval picks the left list of each pair.
Stop at amount - interval: this ensures i + interval < amount, so the partner index never goes past the end. That's why the left-over list (L4) is skipped instead of crashing.
Number of rounds: interval doubles each time, so there are about log₂ k rounds (3 for k = 5). Each round touches every node at most once, which gives O(N log k).'''