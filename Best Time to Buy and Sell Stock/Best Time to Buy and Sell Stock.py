class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # max_profit = 0
        # for i in range(len(prices)-1):
        #     max_profit =  max(max_profit, (max(prices[i+1:]) - prices[i]))
        # return max_profit

        l,  r = 0, 1
        max_profit = 0
        while r <= len(prices)-1:
            if prices[l] - prices[r] >= 0:
                l = r
                r += 1
            else:
                max_profit = max(max_profit, prices[r] - prices[l])
                r += 1
        return max_profit