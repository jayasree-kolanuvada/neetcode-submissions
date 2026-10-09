class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        rows, cols = len(matrix), len(matrix[0])
        self.prefix = [[0] * (cols) for _ in range (rows)]
        for i in range (rows):
            self.prefix[i][0] = matrix[i][0]
            for j in range (1,cols):
                self.prefix[i][j] = matrix[i][j] + self.prefix[i][j-1]
        
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        ans = 0
        for j in range (row1,row2+1):
            if col1 == 0:
                rowSum = self.prefix[j][col2]
            else:
                rowSum = self.prefix[j][col2] - self.prefix[j][col1-1]
            ans += rowSum
        return ans

        
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)


