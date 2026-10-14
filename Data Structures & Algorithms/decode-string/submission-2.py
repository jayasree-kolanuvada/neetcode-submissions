class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for ch in s:
            if ch != "]":
                stack.append(ch)
                continue
            else:
                word = num = ""
                while stack[-1] != "[":
                    word = stack.pop()+word
                stack.pop()
                while stack and stack[-1].isdigit():
                    num = stack.pop()+num
                num = int(num)
                stack.append(word * num)
        return "".join(stack)
        