class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k%n
        nums[:] = nums[-k:] + nums[:-k]
# we do -k cuz last k elements we want
# take o(n) space cuz in python slicing creates a new list 
        