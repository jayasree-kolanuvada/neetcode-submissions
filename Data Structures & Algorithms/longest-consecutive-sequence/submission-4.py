class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set()
        count = maximum = 0
        for num in nums:
            seen.add(num)
        for num in seen:
            if num-1 in seen:
                continue 
            count=1
            while num+1 in seen:
                count+=1
                num+=1
            maximum = max(maximum,count)
        return maximum

