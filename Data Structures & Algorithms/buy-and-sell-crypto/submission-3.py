class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        left = 0

        for right in range(len(prices)):
            if prices[right] > prices[left]:
               maxProfit = max(maxProfit, prices[right] - prices[left])
            elif prices[right] == prices[left]:
                continue
            else:
                left = right
        
        return maxProfit