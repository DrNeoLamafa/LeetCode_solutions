class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        for col in range(n):
            tmp = []
            for row in range(n):
                tmp.append(matrix[row][col])
            matrix.append(tmp[::-1])
        matrix[:] = matrix[n:]