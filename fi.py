user_choice = "Withdraw Cash"
if user_choice == "Withdraw Cash":
    amount = float(input("Enter the amount to withdraw: "))  
    if amount % 10 == 0:
        print("amount",amount)
        print("Thank you for using the ATM.")
    else:
    
        print("Please enter a multiple of 10.")