class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0
        h = len(matrix)-1
        n = len(matrix[0]) - 1
        r = -1

        while l <= h:
            m = l + (h-l)//2
            if target >= matrix[m][0] and target <= matrix[m][n]:
                r = m
                break
            elif target > matrix[m][n]:
                l = m+1
            elif target < matrix[m][0]:
                h = m-1
        if r == -1:
            return False
        l = 0
        h = n

        while l <= h:
            m = l +(h-l)//2
            if target == matrix[r][m]:
                return True
            elif target > matrix[r][m]:
                l = m+1
            else:
                h = m-1
        return False

        