class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        lt = rt = 0
        maxProfit = 0

        while (rt < len(prices)):
            maxProfit = max(maxProfit, prices[rt] - prices[lt])
            if prices[rt] < prices[lt]:
                lt = rt 
            
            rt += 1
        
        return maxProfit