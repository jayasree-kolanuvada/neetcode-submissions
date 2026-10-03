class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        for num in nums:
            index = abs(num)-1
            if nums[index] < 0:
                return abs(num)
            nums[index] *= -1
        # since numbers are in the range 1 to n, for every num we can flip the sign of the number at that corresponding index. if we ever go to a index and num there is already -ve we know that is the duplicate.




    