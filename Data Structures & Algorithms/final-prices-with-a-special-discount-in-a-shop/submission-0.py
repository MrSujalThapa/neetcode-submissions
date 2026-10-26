class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        
        stack = []
        left = 0
        right = 0

        for right in range(1, len(prices)):
            if prices[left] >= prices[right]:
                stack.append(prices[left] - prices[right])
            else:
                stack.append(prices[left])
            left += 1
        
        stack.append(prices[right])
        
        return stack