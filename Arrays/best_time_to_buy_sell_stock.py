class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # buy_sell = tuple()
        # profit = 0

        # for i in range(len(prices)-1):
        #     for j in range(i+1, len(prices)):
        #         if prices[j] > prices [i]:
        #             loop_profit = prices[j] - prices[i]
        #             if loop_profit > profit:
        #                 profit = loop_profit
        #                 buy_sell = (i, j)
        
        # return profit
        
        ## APPROACH -> Difference method 

        # if len(prices) == 1:
        #     return 0

        # diff_arr = list()

        # for i in range(len(prices) - 1):
        #     diff_arr.append(prices[i+1] - prices[i])
        
        # print(diff_arr)

        # # NOW FIND MAX SUBSET OF difference array

        # max_sub = diff_arr[0]
        # result = diff_arr[0]

        # for i in range(1, len(diff_arr)):
        #     max_sub = max(diff_arr[i], max_sub + diff_arr[i])

        #     result = max(result, max_sub)
        
        # if result < 0:
        #     return 0

        # return result\

        ## LINEAR APPROACH

        buy = prices[0]
        max_profit = 0

        for price in prices[1:]:
            if price < buy:
                buy = price
            elif price-buy > max_profit:
                max_profit = price-buy
        
        return max_profit