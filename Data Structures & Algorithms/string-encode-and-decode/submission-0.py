class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for st in strs:
            n = len(st)
            n = str(n)
            res += n + "#" + st
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        n = len(s)
        while i < n:
            length = ""
            while s[i] != "#":
                length += s[i]
                i += 1
            i += 1
            length = int(length)
            word = ""
            while length > 0:
                word += s[i]
                length -= 1
                i += 1
            res.append(word)
        return res



