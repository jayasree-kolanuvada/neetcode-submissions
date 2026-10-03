class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count1 = [0]*26
        count2 = [0]*26

        if len(s1) > len(s2):
            return False 

        for char in s1:
            count1[ord(char)-97] += 1

        matches = sum(1 for i in range(26) if count1[i] == count2[i])
        l = r = 0
        for r in range (len(s2)):
            posr = ord(s2[r])-97
            count2[posr]+=1
            if count2[posr] == count1[posr]:
                matches+=1
            elif count2[posr] == count1[posr]+1: # we cannot use ">" here because it will fire every time the count is greater. we need to capture the transition so it should fire only the first time the count becomes greater.
                matches -= 1

            if (r-l+1) > len(s1):
                posl = ord(s2[l]) - 97
                count2[posl] -= 1

                if count2[posl] == count1[posl]:
                    matches += 1
                elif count2[posl] + 1 == count1[posl]: # be careful here , we add 1 to count2 because we are decrementing from count2 and want to check when the count decreases below count1
                    matches -= 1
                l+=1
            if matches == 26:
                return True 
        return False