class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        mydict = dict()
        t = len(nums)//2
        for num in nums:
            mydict[num] = mydict.get(num,0)+1
            if mydict[num]>t:
                return num

        