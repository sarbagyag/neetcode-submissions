class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit=0
        profit=0
        b,s=0,1

        while(s<=len(prices)-1):
            profit=prices[s]-prices[b]
            if(profit>maxProfit):
                maxProfit=profit
            
            if profit<=0:
                profit=0
                b=s
                s=s+1
            else:
                s=s+1
        return maxProfit


