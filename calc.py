import csv, sys
from collections import deque, namedtuple

Trade = namedtuple("Trade", ["date", "type", "quantity", "price", "fee"])

def load_trades(path):
    trades = []
    with open(path, newline="") as f:
        for row in csv.DictReader(f):
            trades.append(Trade(
                date=row["date"],
                type=row["type"],
                quantity=int(row["quantity"]),
                price=float(row["price"]),
                fee=float(row["fee"])
            ))
    return trades

def calculate_profit(trades):
    inventory = deque()
    total = 0.0
    for t in sorted(trades, key=lambda x: x.date):
        if t.type == "buy":
            inventory.append([t.quantity, t.price])
        else:  # sell
            qty = t.quantity
            while qty > 0:
                bought_qty, bought_price = inventory[0]
                used = min(bought_qty, qty)
                total += (t.price - bought_price) * used
                inventory[0][0] -= used
                qty -= used
                if inventory[0][0] == 0:
                    inventory.popleft()
            total -= t.fee
    return total

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python calc.py transactions.csv")
        sys.exit(1)
    trades = load_trades(sys.argv[1])
    profit = calculate_profit(trades)
    print(f"Total profit: ¥{profit:,.2f}")
