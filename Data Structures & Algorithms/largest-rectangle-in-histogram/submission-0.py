class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxarea = 0
        stack = []

        for i, height in enumerate(heights):
            start = i
            while stack and stack[-1][1] > height:
                index, h = stack.pop()
                maxarea = max(maxarea, h*(i-index))
                start = index
            stack.append((start,height))
        
        for i,h in stack:
            maxarea = max(maxarea, (len(heights)-i)*h)
        return maxarea


        