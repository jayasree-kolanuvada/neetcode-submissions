class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = sum = 0
        mini = float("inf")
        for r in range (len(nums)):
            sum += nums[r]
            while sum >= target:
                mini = min(mini,r-l+1)
                sum -= nums[l]
                l += 1
        if mini == float("inf"):
            mini = 0
        return mini


        