class Solution:
    def isValid(self, s: str) -> bool:
        open = ["(","{","["]
        close = [")","}","]"]
        stack = []

        for bracket in s:
            if bracket in close:
                if len(stack)==0:
                    return False
                check = stack.pop()
                if check not in open:
                    return False
                elif open.index(check) != close.index(bracket):
                    return False 
            elif bracket in open:
                stack.append(bracket)
        return len(stack)==0

        