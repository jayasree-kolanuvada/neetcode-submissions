class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix = dict()
        prefix[0] = 1
        sum = res = 0
        for num in nums:
            sum += num
            if sum - k in prefix:
                res += prefix[sum-k]
            prefix[sum] = prefix.get(sum,0)+1
        return res

            

        
        