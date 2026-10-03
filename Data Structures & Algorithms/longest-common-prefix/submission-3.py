class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]
        for str in strs:
            if len(prefix)>len(str):
                prefix = prefix[:len(str)]
            for i in range (min(len(prefix),len(str))):
                if str[i] != prefix[i]:
                    prefix = prefix[:i]
                    break
        return prefix

        