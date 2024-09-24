class Solution(object):
    def maxProfit(self, prices):
        mini_num=float('inf')
        max_profit=0
        for price in prices:
            if price <mini_num:
                mini_num=price
            profit=price-mini_num
            if profit>max_profit:
                max_profit=profit
        return max_profit
                