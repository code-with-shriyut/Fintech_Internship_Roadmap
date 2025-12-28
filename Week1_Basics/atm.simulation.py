current_balance = 10000
print(f"Current Balance: Rs.{current_balance}")
withdraw_amount = int(input("Welcome to Fintech Bank! Enter amount to withdraw: "))
remaining_balance = current_balance - withdraw_amount
if withdraw_amount > current_balance:
    print("Insufficient Funds! Transaction Failed.")
elif withdraw_amount < 0:
    print("Invalid Amount!")
else:
    print(f"Transaction Sucessful! Remaining Balance: Rs.{remaining_balance}")