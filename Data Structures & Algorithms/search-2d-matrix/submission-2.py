class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = 0
        for i in range(len(matrix)):
            if target <= matrix[i][-1]:
                row = i
                break
        
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
