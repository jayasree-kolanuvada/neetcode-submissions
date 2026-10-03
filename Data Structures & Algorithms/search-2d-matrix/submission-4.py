class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])

        l, r = 0, ROWS * COLS - 1
        while l <= r:
            m = l + (r - l) // 2
            row, col = m // COLS, m % COLS
            if target > matrix[row][col]:
                l = m + 1
            elif target < matrix[row][col]:
                r = m - 1
            else:
                return True
        return False

    # Because the matrix is sorted row-wise and each row is sorted left-to-right, the entire matrix behaves like one big sorted array.
# If we imagine flattening the matrix into a single list, the order of elements doesn't change.

# This means we can run one binary search from index 0 to ROWS * COLS - 1.
# For any mid index m, we can map it back to the matrix using:

# row = m // COLS
# col = m % COLS
# This lets us access the correct matrix element without actually flattening the matrix.