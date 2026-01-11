#  -> I rotated the matrix by first reversing it vertically (top ↔ bottom rows) and then transposing it (swap matrix[row][col] with matrix[col][row]), achieving a 90° clockwise rotation in-place.

#  -> Time Complexity : O(n^2) - Both the row reversal and the transpose traverse the entire n × n matrix once.

#  -> Space Complexity : O(1) - The rotation is done in-place using only a temporary variable, with no extra data structures.👇

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        edge_length = len(matrix)

        top = 0
        bottom = edge_length - 1

        while top < bottom:
            for col in range(edge_length):
                temp = matrix[top][col]
                matrix[top][col] = matrix[bottom][col]
                matrix[bottom][col] = temp
            top += 1
            bottom -= 1

        for row in range(edge_length):
            for col in range(row+1, edge_length):
                temp = matrix[row][col]
                matrix[row][col] = matrix[col][row]
                matrix[col][row] = temp
        
        return matrix