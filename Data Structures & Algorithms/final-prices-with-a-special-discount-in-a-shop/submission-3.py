class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        
        stack = []
        left = 0
        right = 1

        while len(stack) < len (prices):
            if right >= len(prices):
                stack.append(prices[left])
                left += 1
                right = left
            elif prices[left] >= prices[right]:
                stack.append(prices[left] - prices[right])
                left += 1
                right = left
            right += 1
        
       # stack.append(prices[-1])
        
        return stack