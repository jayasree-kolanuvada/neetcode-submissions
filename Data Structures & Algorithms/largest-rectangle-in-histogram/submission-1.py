class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxarea = 0
        for i , height in enumerate(heights):
            start = i
            while stack and height < stack[-1][1]:
                index, h = stack.pop()
                area = (i - index)*h
                maxarea = max(maxarea,area)
                start = index
            stack.append([start,height])
            n = len(heights)
        for i,h in stack:
            maxarea = max(maxarea,(n-i)*h)
        return maxarea



        