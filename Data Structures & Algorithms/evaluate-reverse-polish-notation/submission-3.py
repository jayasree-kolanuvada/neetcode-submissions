class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token in "+*-/":
                first = stack.pop()
                second = stack.pop()
                if token == "+":
                    ans = first + second
                elif token == "*":
                    ans = first * second
                elif token == "-":
                    ans = second - first 
                else:
                    ans = int(second / first )
                stack.append(ans)
            else:
                stack.append(int(token))
        return stack[-1]
        