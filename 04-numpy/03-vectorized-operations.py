import numpy as np

prices = np.array([100, 200, 150, 300, 250], dtype = float)

print("Original prices:", prices)

#1. increase all by 10%
increased_prices = prices * 1.10
print("Prices after 10% increase: ", increased_prices)

#2. minus all by 20
reduced_prices = prices - 20
print("Prices after minus by 20: ", reduced_prices)

#3. sum
print("Sum: ", prices.sum())

#4. average
print("Average price:", prices.mean())

#5. min and max
min_price = prices.min()
max_price = prices.max()
print("Minimum price:", min_price)
print("Maximum price:", max_price)

#6. normalization
if min_price == max_price:
    normalized_prices = np.zeros_like(prices)
else:
    normalized_prices = (prices - min_price) / (
    max_price - min_price)

print("Normaized prices:", normalized_prices)

#7. round
rounded_normalized_prices = np.round(normalized_prices, 2)
print("Rounded normalized prices:", rounded_normalized_prices)

#8. check original array
print("Original prices after operations:", prices)