class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        
        min_price = float("inf")
        max_profit = 0
        
        for i in range(len(prices)):            
            if prices[i] < min_price:
                min_price = prices[i]
              
              
            if  prices[i]-min_price > max_profit:
                max_profit = prices[i] - min_price
            
        return max_profit
    
    
    


# prices = [7,1,5,3,6,4]

prices =[3,2,6,5,0,3]
s1 = Solution()
print(s1.maxProfit(prices))