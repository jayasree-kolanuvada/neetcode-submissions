class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        i = j = 0
        while i < len(word) and j < len(abbr):
            c = abbr[j]
            if c.isdigit():
                if c == '0':  # leading zero not allowed
                    return False
                num = 0
                while j < len(abbr) and abbr[j].isdigit():
                    num = num * 10 + int(abbr[j])
                    j += 1
                i += num
            else:
                if word[i] != c:
                    return False
                i += 1
                j += 1
        return i == len(word) and j == len(abbr)
        