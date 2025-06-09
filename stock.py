import datetime

stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 140,
    "AMZN": 130,
    "MSFT": 310
}

portfolio = {}
total_investment = 0

print("Welcome to the Stock Portfolio Tracker!")
print("Available stocks and prices:")
for stock, price in stock_prices.items():
    print(f"{stock}: ${price}")

while True:
    symbol = input("\nEnter stock symbol (or 'done' to finish): ").upper()
    if symbol == 'DONE':
        break
    if symbol not in stock_prices:
        print("Invalid stock symbol. Try again.")
        continue
    try:
        qty = int(input(f"Enter quantity of {symbol}: "))
        if qty < 0:
            print("Quantity must be non-negative.")
            continue
        portfolio[symbol] = portfolio.get(symbol, 0) + qty
    except ValueError:
        print("Invalid quantity. Enter a number.")

print("\n--- Portfolio Summary ---")
print(f"{'Stock':<6} {'Qty':<5} {'Unit Price($)':<14} {'Total Cost($)':<14}")
print("-" * 45)

for symbol, qty in portfolio.items():
    price = stock_prices[symbol]
    cost = price * qty
    total_investment += cost
    print(f"{symbol:<6} {qty:<5} {price:<14} {cost:<14}")

print("-" * 45)
print(f"{'Total Investment:':<25} ${total_investment}")

save = input("\nDo you want to save this summary to CSV? (yes/no): ").lower()
if save == 'yes':
    filename = f"portfolio_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
    with open(filename, "w") as f:
        f.write("Stock,Quantity,Unit Price,Total Cost\n")
        for symbol, qty in portfolio.items():
            price = stock_prices[symbol]
            cost = price * qty
            f.write(f"{symbol},{qty},{price},{cost}\n")
        f.write(f"Total,,,{total_investment}\n")
    print(f"Portfolio saved as '{filename}'")