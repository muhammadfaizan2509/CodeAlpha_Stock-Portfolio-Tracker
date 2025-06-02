# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "AMZN": 130,
    "MSFT": 320
}

portfolio = {}
total_investment = 0

print("Welcome to the Stock Portfolio Tracker!\n")
print("Available stocks and prices:")
for stock, price in stock_prices.items():
    print(f"{stock}: ${price}")
print("\nEnter your stock holdings. Type 'done' to finish.\n")

# Input loop
while True:
    stock_name = input("Enter stock symbol (e.g., AAPL): ").upper()
    if stock_name == "DONE":
        break

    if stock_name not in stock_prices:
        print("Stock not found in price list. Try again.\n")
        continue

    try:
        quantity = int(input(f"Enter quantity of {stock_name}: "))
        if quantity < 0:
            raise ValueError
        portfolio[stock_name] = portfolio.get(stock_name, 0) + quantity
        print(f"Added {quantity} shares of {stock_name}.\n")
    except ValueError:
        print("Invalid quantity. Please enter a positive integer.\n")

# Calculate total investment
print("\n----- Portfolio Summary -----")
for stock, qty in portfolio.items():
    value = qty * stock_prices[stock]
    total_investment += value
    print(f"{stock}: {qty} shares x ${stock_prices[stock]} = ${value}")

print(f"\nTotal Investment Value: ${total_investment}")

# Optional: Save to a file
save = input("\nDo you want to save this to a file? (yes/no): ").lower()
if save == "yes":
    filename = "portfolio_summary.txt"
    with open(filename, "w") as f:
        f.write("Stock Portfolio Summary\n")
        for stock, qty in portfolio.items():
            value = qty * stock_prices[stock]
            f.write(f"{stock}: {qty} shares x ${stock_prices[stock]} = ${value}\n")
        f.write(f"\nTotal Investment Value: ${total_investment}\n")
    print(f"Portfolio saved to '{filename}'.")
