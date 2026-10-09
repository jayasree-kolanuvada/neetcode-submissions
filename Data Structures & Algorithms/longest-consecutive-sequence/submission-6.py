class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        maxlength = 0
        for s in seen:
            longest = 1
            if s-1 in seen:
                continue
            while s+1 in seen:
                longest += 1
                s+=1
            maxlength = max(maxlength,longest)
        return maxlength 
    

        