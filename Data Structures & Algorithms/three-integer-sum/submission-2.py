class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        freqmap = defaultdict(int)
        for num in nums:
            freqmap[num]+=1 
        for i in range (len(nums)-1):
            freqmap[nums[i]]-=1 # need to decrment here , cannot decrement in inner loop cuz that would decrease 1 i for each j
            if i>0 and nums[i]==nums[i-1]:
                continue # checking for duplicate i value , need to check if i>0 otherwise might get error when i=0. can also do "if i" which is just a short hand check for "if i!=0"
            for j in range (i+1,len(nums)):
                freqmap[nums[j]]-=1
                if j-1 > i and nums[j]==nums[j-1]:
                    continue # check for duplicates 
                currsum = nums[i]+nums[j]
                if freqmap[0-currsum] > 0:
                    ans.append([nums[i], nums[j], 0-currsum])
            for j in range (i+1,len(nums)):
                freqmap[nums[j]]+=1 # restoring the count of all elements before the new i loop starts 
        return ans





       

