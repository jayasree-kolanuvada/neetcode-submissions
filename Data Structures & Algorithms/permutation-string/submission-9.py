class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count1 = dict()
        count2 = dict()
        l = 0
        for ch in s1:
            count1[ch] = count1.get(ch,0)+1
        for r in range (len(s2)):
            if s2[r] not in count1:
                l = r+1
                count2 = dict()
                continue
            if (r-l+1) > len(s1):
                count2[s2[l]]-=1
                l += 1
            count2[s2[r]] = count2.get(s2[r],0)+1
            if count1 == count2:
                return True
        return False
        