class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        rows = (len(matrix) + 1) // 2
        cols = len(matrix) // 2
        for i in range(rows):
            for j in range(cols):
                temp1 = matrix[j][len(matrix) - i - 1]
                matrix[j][len(matrix) - i - 1] = matrix[i][j]
                temp2 = matrix[len(matrix) - i - 1][len(matrix) - j - 1]
                matrix[len(matrix) - i - 1][len(matrix) - j - 1] = temp1
                temp1 = matrix[len(matrix) - j - 1][i]
                matrix[len(matrix) - j - 1][i] = temp2
                matrix[i][j] = temp1
        
