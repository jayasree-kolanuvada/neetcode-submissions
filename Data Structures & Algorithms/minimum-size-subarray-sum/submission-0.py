class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        r = l = add = 0
        mini = float('inf')
        while l <= r and l < len(nums):
            if add >= target:
                mini = min(mini, r-l)
                add -= nums[l]
                l+=1
                continue
            if r < len(nums):
                add += nums[r]
                r+=1
            if r == len(nums) and add < target:
                break
        if mini == float('inf'):
            return 0
        return mini

            
            




        
        