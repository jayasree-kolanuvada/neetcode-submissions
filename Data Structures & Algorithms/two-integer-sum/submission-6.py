class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        a = dict()
        for i,num in enumerate(nums):
            curr = target - num
            if curr in a:
                return [a.get(curr),i]
            else:
                a[num] = i

