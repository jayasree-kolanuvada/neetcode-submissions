class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        r = l = add = 0
        mini = float('inf') # cannot set mini to 0
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
                break # this is in case l gets stuck and never reaches end of aarray like when sum is small and we have already reached end of array with r so there is no way we can increase sum
        if mini == float('inf'):
            return 0
        return mini

            
            




        
        