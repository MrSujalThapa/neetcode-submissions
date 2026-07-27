class Solution:
    def arrangeCoins(self, n: int) -> int:
        #lowk quadratic formula would be much more efficient
        left = 1
        right = n 

        while left <= right:
            middle = (left + right) // 2
            coins_needed = middle * (middle + 1) // 2

            if coins_needed == n:
                return middle
            elif coins_needed < n:
                left = middle + 1
            else:
                right = middle - 1

        return right