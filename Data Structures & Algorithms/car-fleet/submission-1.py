import math
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        ps = []
        time = [0] * len(position)
        stack = []
        for i in range(len(position)):
            ps.append((position[i],speed[i]))
        ps.sort(key = lambda x:x[0])
        for i in range(len(ps)):
            distance = target - ps[i][0]
            time[i] = distance / ps[i][1]
        for i in range (len(time)):
            while stack and stack[-1] <= time[i]:
                stack.pop()
            stack.append(time[i])
        return len(stack)



            #[3,4,5,6,7,8]
            #[2,2,2,1,1,1]




        