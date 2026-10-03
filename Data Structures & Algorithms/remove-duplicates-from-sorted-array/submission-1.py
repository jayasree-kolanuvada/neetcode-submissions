class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        p1 = 0
        p2 = 0

        while p1<len(nums)-1 and nums[p1]!=nums[p1+1]:
            p1+=1
        if p1 >= len(nums):
            return p1+1
        p2=p1+1

        while p2 < len(nums):
            if nums[p2] != nums[p1]:
                nums[p1+1] = nums[p2]
                p1+=1
                p2+=1
            else:
                p2+=1
        return p1+1



        