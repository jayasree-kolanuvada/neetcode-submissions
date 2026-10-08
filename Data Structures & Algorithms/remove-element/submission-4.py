class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        l = k = 0
        for l in range (len(nums)):
            if nums[l] != val:
                nums[k] = nums[l]
                k += 1
        return k

        