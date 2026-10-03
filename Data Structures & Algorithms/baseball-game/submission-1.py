class Solution:
    def calPoints(self, operations: List[str]) -> int:
        res = []
        sum = 0
        for op in operations:
            if op.lstrip('-').isdigit():
                res.append(int(op))
            elif op == "+":
                add = res[-1]+res[-2]
                res.append(add)
            elif op == "D":
                double = res[-1]*2
                res.append(double)
            elif op == "C":
                res.pop()
        for num in res:
            sum+=num
        return sum
        