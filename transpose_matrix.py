class Solution:
    def transpose(self, matrix):
        if not matrix:
            return []

        # Get dimensions of the input matrix
        rows, cols = len(matrix), len(matrix[0])

        # Initialize the transposed matrix
        transposed = [[0] * rows for _ in range(cols)]

        # Fill the transposed matrix
        for i in range(rows):
            for j in range(cols):
                transposed[j][i] = matrix[i][j]

        return transposed

