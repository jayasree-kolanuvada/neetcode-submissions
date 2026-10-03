class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]
        for i in range(1, len(strs)):
            j = 0
            while j < min (len(strs[i]),len(prefix)):
                if strs[i][j] != prefix[j]:
                    break
                j+=1
            prefix = prefix[:j]
        return prefix




        