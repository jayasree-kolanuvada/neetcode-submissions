class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [0]*len(nums)
        prod = 1
        zero = 0
        for num in nums:
            if num == 0:
                zero+=1
            else:
                prod = prod*num
        if zero > 1:
            return [0]*len(nums)
        for i in range(len(nums)):
            if zero == 1: 
                if nums[i] == 0:
                    ans[i] = prod
                else:
                    ans[i] = 0
            else:
                ans[i] = prod//nums[i]
        return ans

        
        


