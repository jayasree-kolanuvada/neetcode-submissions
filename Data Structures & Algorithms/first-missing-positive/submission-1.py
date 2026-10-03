#class Solution:
    
    # def firstMissingPositive(self, nums: List[int]) -> int:
    #    i=0
    #    while i < len(nums):
    #        if nums[i] <= 0:
    #            i+=1
    #            continue
    #        x = nums[nums[i]-1]
    #        nums[nums[i]-1] = 0
    #        while x > 0:
    #            y = nums[x-1]
    #            nums[x-1] = 0
    #            x=y
    #        i+=1
    #    for i in range (len(nums)):
    #        if nums[i]>0:
    #            return i+1
    #    return len(nums)+1 """

        # cannot simply make the numbers 0 cuz that would lead in information loss. for example [1,2,0] would become [0,0,0] and your solution would incorrectly return 4 , when it is supposed to return 3. 
        # also look out for index out of range error 
        # for [-2,-1,0] it would completely skip the loop and return n+1

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        missing = 1
        while True:
            flag = True
            for num in nums:
                if missing == num:
                    flag = False
                    break

            if flag:
                return missing
            missing += 1
        
        

        