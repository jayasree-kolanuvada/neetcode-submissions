
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range (n):
            if nums[i] < 0:
                nums[i] = 0
        for i in range (n):
            target = (abs(nums[i]))-1
            if 1 <= target+1 <= n:
                if nums[target] > 0:
                    nums[target]*=-1
                elif nums[target] == 0:
                    nums[target] = -1 * (n+1)
        for i in range(1, n + 1):
            if nums[i - 1] >= 0:
                return i

        return len(nums) + 1



        
        

        