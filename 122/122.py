class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
        # [1,2,3,4,5]
        # 2 - 1 = 1
        # 3 - 2 = 1
        # 4 - 3 = 1
        # 4 - 5 = 1
        # If buying at I and selling at i + 1 makes money do it (greedy)
        profit = 0
        for i in range(len(prices)-1):
            if prices[i+1] - prices[i] > 0:
                profit += prices[i+1] - prices[i]
        

        return profit