class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = r = 0
        seen = dict()
        maxf = res = 0
        while r < len(s):
            seen[s[r]] = seen.get(s[r],0)+1
            if seen[s[r]]>maxf:
                maxf = seen[s[r]]
            while (r - l + 1) - maxf > k:
                seen[s[l]]-=1
                l += 1
            res = max(res,r-l+1)
            r += 1
        return res       

        