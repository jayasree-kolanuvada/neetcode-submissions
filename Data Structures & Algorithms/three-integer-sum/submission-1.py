class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        for i in range (len(nums)-2):
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l = i+1
            r = len(nums)-1
            while l<r:
                currsum = nums[i]+nums[l]+nums[r]
                if currsum > 0:
                    r-=1
                elif currsum < 0:
                    l+=1
                else:
                    triplet = [nums[i],nums[l],nums[r]]
                    if triplet not in ans:
                        ans.append(triplet)
                    l+=1
                    r-=1
        return ans


       

