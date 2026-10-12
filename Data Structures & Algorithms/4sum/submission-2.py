class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        count = collections.defaultdict(int)
        ans = []

        for num in nums:
            count[num] += 1
        
        for i in range (len(nums)):
            count[nums[i]] -= 1
            if i and nums[i] == nums[i-1]:
                continue
            for j in range(i+1,len(nums)):
                count[nums[j]] -= 1
                if j > i+1 and nums[j]==nums[j-1]:
                    continue
                for k in range(j+1,len(nums)):
                    count[nums[k]] -= 1
                    if k > j+1 and nums[k] == nums[k-1]:
                        continue 
                    sum = nums[i]+nums[j]+nums[k]
                    find = target - sum
                    if count[find] > 0:
                        ans.append([nums[i],nums[j],nums[k],find])
                for l in range (j+1,len(nums)):
                    count[nums[l]] += 1
            for r in range(i+1,len(nums)):
                count[nums[r]] += 1
        return ans


                
        