class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums)-1
        mini = float('inf')
        while l <= r:
            if nums[l] < nums[r]:
                mini = min(mini,nums[l])
                break
            m = (l+r) // 2
            mini = min(mini,nums[m])
            if nums[m] >= nums[l]:
                l = m+1
            else:
                r = m-1
        return mini

        
        #[0,1,2,3,4,5,6]
        #[6,0,1,2,3,4,5]
        #[5,6,0,1,2,3,4]
        #[4,5,6,0,1,2,3]
        #[3,4,5,6,0,1,2]
        #[2,3,4,5,6,0,1]
        #[1,2,3,4,5,6,0]