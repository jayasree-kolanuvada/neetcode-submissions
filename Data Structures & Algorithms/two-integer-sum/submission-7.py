class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        fmap = collections.defaultdict()
        for i, num in enumerate(nums):
            if target - num in fmap:
                return [fmap[target - num], i]
            fmap[num] = i

