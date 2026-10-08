class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        list1 = [0] * 26
        list2 = [0] * 26
        for char in s:
            index = ord(char) - ord("a")
            list1[index]+=1
        for char in t:
            index = ord(char) - ord("a")
            list2[index]+=1
        return list1 == list2

        