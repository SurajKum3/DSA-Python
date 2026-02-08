#  -> Used Dynamic Programming with space optimization, where each cell’s value is computed as the sum of paths from the top and left, while keeping only the previous row to reduce memory usage.

#  -> Time Complexity : O(m × n) - Each cell in the m × n grid is computed exactly once.

#  -> Space Complexity : O(n) - Instead of storing the full 2D DP table, only two 1D arrays (previous row and current row) of size n are used.👇

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        aboveRow = [1] * n

        for _ in range(m - 1):
            currentRow = [1] * n
            for i in range(1, n):
                currentRow[i] = currentRow[i-1] + aboveRow[i]
            aboveRow = currentRow
        
        return aboveRow[-1]