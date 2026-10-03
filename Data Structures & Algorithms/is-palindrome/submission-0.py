class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        new = "".join(char.lower() for char in s if char.isalnum())
        r = len(new)-1
        while l<r:
            if new[l]!=new[r]:
                return False 
            l+=1
            r-=1
        return True

        