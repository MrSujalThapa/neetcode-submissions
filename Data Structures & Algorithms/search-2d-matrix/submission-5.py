class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left = 0
        right = len(matrix) - 1
        row = 0
        while left <= right:
            middle = (left + right) // 2
            if matrix[middle][-1] < target:
                left = middle + 1
            else:
                right = middle - 1

        row = left
        if row == len(matrix):
            return False
        left = 0
        right = len(matrix[row]) - 1

        while left <= right:
            middle = (left + right) // 2
            if matrix[row][middle] < target:
                left = middle + 1
            elif matrix[row][middle] == target:
                return True
            else:
                right = middle - 1

        return False
