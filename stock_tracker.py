stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 150,
    "MSFT": 300
}

total = 0

print("=== Stock Portfolio Tracker ===")

while True:
    stock = input("Enter stock name (AAPL/TSLA/GOOG/MSFT or EXIT): ").upper()

    if stock == "EXIT":
        break

    if stock in stock_prices:
        qty = int(input("Enter quantity: "))
        value = stock_prices[stock] * qty
        total += value
        print("Investment:", value)
    else:
        print("Stock not available.")

print("\nTotal Investment =", total)

with open("portfolio.txt", "w") as file:
    file.write("Total Investment = " + str(total))

print("Saved to portfolio.txt")