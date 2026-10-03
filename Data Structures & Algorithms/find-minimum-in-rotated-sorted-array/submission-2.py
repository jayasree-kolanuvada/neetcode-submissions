class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            m = l + (r - l) // 2
            if nums[m] < nums[r]:
                r = m
            else:
                l = m + 1
        return nums[l]

        
        #[0,1,2,3,4,5,6]
        #[6,0,1,2,3,4,5]
        #[5,6,0,1,2,3,4]
        #[4,5,6,0,1,2,3]
        #[3,4,5,6,0,1,2]
        #[2,3,4,5,6,0,1]
        #[1,2,3,4,5,6,0]