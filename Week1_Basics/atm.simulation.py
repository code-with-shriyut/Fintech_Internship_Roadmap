user_account = {"name":"Shriyut Janardan","balance": 45000, "acc_type": "Savings"}
while True:
    print("Select '1' to CHECK BALANCE!")
    print("Select '2' to WITHDRAW!")
    print("Select '3' to DEPOSIT!") 
    print("Select '4' to EXIT!")
    user_input = int(input("Enter Your Choice: "))
    if user_input == 1:
        print(f"Current Balance: ₹{user_account['balance']}")
        print("Transaction Completed Sucessfully!!")
    elif user_input == 2:
        withdraw_amount = int(input("Welcome to Fintech Bank! Enter amount to withdraw: "))
        remaining_balance = user_account["balance"] - withdraw_amount
        if withdraw_amount > user_account["balance"]:
           print("Insufficient Funds! Transaction Failed.")
        elif withdraw_amount < 0:
           print("Invalid Amount!")
        else:
           print(f"Transaction Sucessful! Remaining Balance: Rs.{remaining_balance}")
           user_account["balance"] = remaining_balance
           print(user_account)
    elif user_input == 3:
        depositing_amount = int(input("Enter the amount you want to deposit: ₹"))
        user_account["balance"] = user_account["balance"] + depositing_amount
        print(user_account)
        print("Transaction Completed Sucessfully!!")
    elif user_input == 4:
        print("Thank You for using Fintech Bank. Goodbye!!")
        break
    else:
     
     print("Invalid input!! Please enter a valid input.")







