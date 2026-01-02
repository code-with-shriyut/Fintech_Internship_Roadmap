transactions = [5000, -2000, 2500, 6000, -1000, 500, -2000]
total_balance = 0
print("--- MINI STATEMENT ---")
for t in transactions:
    if t > 0:
        print(f"CREDIT ₹{t}")
    else:
        print(f"DEBIT ₹{abs(t)}")
    total_balance = total_balance + t
print("----------------------")
print(f"Net Balance: ₹{total_balance}")
