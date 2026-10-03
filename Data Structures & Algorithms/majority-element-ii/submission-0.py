class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        freq = dict()
        ans = set()
        t = len(nums)//3
        for num in nums:
            freq[num] = freq.get(num,0)+1
            if freq[num] > t:
                ans.add(num)
        return list(ans)
        