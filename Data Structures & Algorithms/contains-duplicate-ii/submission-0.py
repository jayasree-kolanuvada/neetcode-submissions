class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        l = r = 0
        seen = set()

        if k == 0:
            return False 
        while r < len(nums):
            if (r-l) > k:
                seen.discard(nums[l])
                l+=1
            else:
                if nums[r] in seen:
                    return True
                seen.add(nums[r])
                r+=1
        return False
            

        