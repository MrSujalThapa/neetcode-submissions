class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        left = 0
        right = num

        while left <= right:
            middle = (left + right) // 2

            val = middle*middle

            if val > num:
                right = middle - 1
            elif val == num:
                return True
            else:
                left = middle + 1
        
        return False
