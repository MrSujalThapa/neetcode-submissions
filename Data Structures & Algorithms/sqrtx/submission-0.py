class Solution:
    def mySqrt(self, x: int) -> int:
        left = 0 
        right = x

        while left <= right:
            middle = (left + right) //2
            val = middle*middle

            if val < x:
                left = middle + 1
            elif val == x:
                return middle
            else:
                right = middle - 1
        
        return right