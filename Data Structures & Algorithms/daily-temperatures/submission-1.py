class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        incstack = []
        res = [0]*len(temperatures)

        for i in range (len(temperatures)-1,-1,-1):
            while incstack and temperatures[i] >= incstack[-1][0]:
                incstack.pop()
            if not incstack:
                incstack.append((temperatures[i],i))
            else:
                res[i] = incstack[-1][1] - i
                incstack.append((temperatures[i],i))
        return res

       