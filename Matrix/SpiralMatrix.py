#  -> I used directional movement (dx, dy) to traverse the matrix in a spiral, marking visited cells (with ".") and changing direction whenever the next move goes out of bounds or hits a visited cell.

#  -> Time Complexity : O(m * n) - Each element of the matrix is visited exactly once during the traversal.

#  -> Space Complexity : O(1) - No extra data structures are used for traversal, the matrix itself is modified to mark visited cells.👇

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        rows, cols = len(matrix), len(matrix[0])
        x, y, dx, dy = 0, 0, 1, 0
        res = []

        for _ in range(rows * cols):
            res.append(matrix[y][x])
            matrix[y][x] = "."

            if not 0 <= x + dx < cols or not 0 <= y + dy < rows or matrix[y+dy][x+dx] == ".":
                dx, dy = -dy, dx
            
            x += dx
            y += dy
        
        return res