class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = []
        for rowNum in range(numRows):
            row = [1]*(rowIndex + 1)
            for i in range(1, rowNum):
                row[i] =  triangle[rowNum - 1][i - 1] + triangle[rowNum - 1][i]

            triangle.append(row)
        