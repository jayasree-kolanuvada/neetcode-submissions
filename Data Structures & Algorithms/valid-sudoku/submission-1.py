class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        freq = set()
        for i in range(9):
            freq.clear()
            for j in range(9):
                if board[i][j] == ".":
                    continue
                if board[i][j] in freq:
                    return False
                else:
                    freq.add(board[i][j])
        freq.clear()

        for i in range (9):
            freq.clear()
            for j in range (9):
                if board[j][i] == ".":
                    continue
                if board[j][i] in freq:
                    return False
                else:
                    freq.add(board[j][i])

        data = [set() for _ in range(9)]
        for i in range (9):
            for j in range (9):
                if board[i][j] == ".":
                    continue
                index = (i//3)*3 + (j//3)
                if board[i][j] in data[index]:
                    return False
                else:
                    data[index].add(board[i][j])
        return True
        

        