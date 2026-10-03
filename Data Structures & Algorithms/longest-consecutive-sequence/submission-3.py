class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        maximum = 0
        for num in seen:
            if num - 1 in seen:
                continue
            else:
                count = 1
                while num+1 in seen:
                    count+=1
                    num+=1
                maximum = max(count,maximum)
        return maximum
        

        