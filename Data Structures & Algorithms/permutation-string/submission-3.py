class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count1 = dict()
        count2 = dict()

        if len(s1) > len(s2):
            return False 

        for char in s1:
            count1[char] = count1.get(char,0)+1

        l = r = 0
        for r in range (len(s2)):
            if s2[r] not in count1:
                l = r + 1 # because on nect turn r will become +1 and if it is valid wont enter the if statement 
                count2 = dict()
                continue
            count2[s2[r]] = count2.get(s2[r],0)+1
            if (r-l+1) > len(s1): # we are maintaining a fixed window of size equal to s1 becasue we need combos of that length only 
                count2[s2[l]] -= 1
                l+=1
            if count1 == count2:
                return True
        return False 

# time complexity would be O(26n) - so even if it is linear time , there is a hidden 26 factor because of checking equality of dictionaries in every iteration
            