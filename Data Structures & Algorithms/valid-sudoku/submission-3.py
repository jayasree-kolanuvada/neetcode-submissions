class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = [set() for _ in range (9)]  
        column = [set() for _ in range (9)]
        box = [set() for _ in range (9)]

        for i in range(9):
            for j in range(9):
                if board[i][j]=='.':
                    continue
                if board[i][j] in row[i]:
                    return False
                row[i].add(board[i][j])
                if board[i][j] in column[j]:
                    return False
                column[j].add(board[i][j])
                if board[i][j] in box[(i//3)*3+(j//3)]:
                    return False 
                box[(i//3)*3+(j//3)].add(board[i][j])
        return True
        