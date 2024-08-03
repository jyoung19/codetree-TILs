n = int(input())
arr = list(map(int, input().split()))

min_price = arr[0]
max_profit = 0

for i in range(1, n):
    price = arr[i]
    profit = price - min_price

    if profit > max_profit:
        max_profit = profit
    
    if price < min_price:
        min_price = price

print(max_profit)