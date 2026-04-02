class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        n = len(matrix)
        m = len(matrix[0])
        ma = []
        for i in range(m):
            l = [matrix[j][i] for j in range(n)]
            ma.append(l)
        return ma