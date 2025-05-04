def buy_profit_time(ls):
    min_price = float('inf')
    max_price = 0

    for j, i in enumerate(ls):
        min_price = min(i, min_price)
        max_price = max(max_price, i - min_price )
    return f"{max_price} on day {j} "
prices = [7, 1, 5, 3, 6, 4]
print(buy_profit_time(prices))
