class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # we can assume the array to be a linked list 
        # this is a linked list problem and we need to know the Floyd's Algorithm that tells us when a cycle starts in a linked list
        slow = fast = nums[0]
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        slow = nums[0]
        while True:
            if slow == fast:
                return slow
            slow = nums[slow]
            fast = nums[fast]
            






    