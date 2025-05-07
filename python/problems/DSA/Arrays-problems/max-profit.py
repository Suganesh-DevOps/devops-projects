'''
Best Time to Buy and Sell Stock
Maximize profit by choosing a single day to buy and another to sell.
'''

def perfect_time_to_buy_and_Sell(ls):
      buy = 0
      sell = 0
      min = float('inf')
      max = 0

      for price in ls:
            if price < min:
                  min = price
            else:
                  max = price
      max_profit = max - min
      return max_profit
ls = [7, 3, 4, 5, 6, 9, 1]
print(perfect_time_to_buy_and_Sell(ls))
