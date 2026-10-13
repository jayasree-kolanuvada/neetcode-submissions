class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        temp = []
        ans = [0] * len(temperatures)
        for i in range(len(temperatures)-1,-1,-1):
            while temp and temperatures[i] >= temp[-1][0]:
                temp.pop()
            if temp:
                ans[i] = temp[-1][1] - i
            temp.append([temperatures[i],i])
        return ans


        