class Solution:
    def findPeakElement(self, nums: list[int]) -> int:
        low , high = 0 , len(nums)-1
        while low < high:
            mid = low + ((high - low)//2)
            if nums[mid] > nums[mid+1]: 
                high = mid # cannot do mid -1 cuz mid itself might be the peak so you never know 
            else:
                low = mid+1
        return low
        