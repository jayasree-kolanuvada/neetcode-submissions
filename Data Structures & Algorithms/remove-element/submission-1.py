class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
     left = 0
     right = len(nums) - 1
     count = 0

     while left < len(nums) and left <= right:
        if nums[left] == val:
            nums[left],nums[right]=nums[right],nums[left]
            right-=1
            count+=1
        else:
            left+=1
     return len(nums) - count
        