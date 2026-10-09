class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            while 0 < nums[i] <= n and nums[i]!=i+1:
                target = nums[i]-1
                if nums[target] == nums[i]:
                    break
                nums[target],nums[i] = nums[i],nums[target]
        for i in range(n):
            if nums[i] != i+1:
                return i+1
        return n+1

            
        