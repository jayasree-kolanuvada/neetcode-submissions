class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        list=[]
        for n in nums:
            if n in list:
                return True
            list.append(n)
        return False

        