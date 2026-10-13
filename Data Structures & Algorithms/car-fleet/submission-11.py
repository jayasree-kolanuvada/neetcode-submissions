class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n = len(position)
        posSpeed = []
        time = [0] * n
        stack = []
        fleet = 1
        for i in range (n):
            posSpeed.append([position[i],speed[i]])
        posSpeed.sort(key = lambda x:x[0])
        for i in range(n):
            distance = target - posSpeed[i][0]
            speed = posSpeed[i][1]
            time[i] = distance / speed
        curr = 0
        for i in range(n-1,-1,-1):
            if stack and time[i] <= curr:
                stack.pop()
            stack.append(time[i])
            if stack[-1] > curr:
                curr = stack[-1]
        return len(stack)
            
            
[0,3,5,8,10]
[1,3,1,4,2]
[12,3,7,1,1]
        