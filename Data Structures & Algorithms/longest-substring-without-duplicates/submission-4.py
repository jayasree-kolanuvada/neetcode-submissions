class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = dict()
        l = r = maxi = 0

        for r in range (len(s)):
            if s[r] in seen and seen[s[r]]>=l:
                l = seen[s[r]]+1
            seen[s[r]] = r
            length = r-l+1
            maxi = max(maxi,length)


        return maxi
        