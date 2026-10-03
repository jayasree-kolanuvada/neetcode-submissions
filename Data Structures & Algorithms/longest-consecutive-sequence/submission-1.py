class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        max = 0
        for num in nums:
            if num - 1 in seen:
                continue
            else:
                count = 1
                while num+1 in seen:
                    count+=1
                    num+=1
                if count > max:
                    max = count
        return max
        

        