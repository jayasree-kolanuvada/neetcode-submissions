class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        mydict1 = dict()
        mydict2 = dict()
        for i in s:
            mydict1[i]=mydict1.get(i,0)+1
        for j in t:
            mydict2[j]=mydict2.get(j,0)+1
        return mydict1 == mydict2

        

        