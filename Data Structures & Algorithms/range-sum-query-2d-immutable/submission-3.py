class NumMatrix:
    # to calculate prefix , we maintain a running prefix sum of the current row we are on and then just add  calculated prefix sum of the above row , that we cover the entire rectangle
    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        rows, cols = len(matrix), len(matrix[0])
        self.prefix = [[0] * (cols+1) for _ in range (rows+1)]
        for i in range(rows):
            sum = 0
            for j in range(cols):
                sum += matrix[i][j]
                above = self.prefix[i][j+1]
                self.prefix[i+1][j+1] = sum + above
        
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        total = self.prefix[row2+1][col2+1]
        up = self.prefix[row1][col2+1]
        side = self.prefix[row2+1][col1]
        topleft = self.prefix[row1][col1]
        ans = total - up - side + topleft
        return ans
        

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)


