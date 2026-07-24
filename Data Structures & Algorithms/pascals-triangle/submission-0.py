class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = []
        for rowIndex in range(numRows):
            row = [1]*(rowIndex + 1)
            for i in range(1, rowIndex):
                row[i] = triangle[rowIndex - 1][i - 1] + triangle[rowIndex - 1][i]
            triangle.append(row)

        return triangle 