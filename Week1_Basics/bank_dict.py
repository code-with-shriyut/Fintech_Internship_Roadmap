user_account = {"name":"Shriyut Janardan","balance": 45000, "acc_type": "Savings"}
print(f"Your Initial Balance: ₹{user_account['balance']}")
depositing_amount = int(input("Enter the amount you want to deposit: ₹"))
user_account["balance"] = user_account["balance"] + depositing_amount
user_account["email"] = "shriyutjanardan@gmail.com"
print(user_account)