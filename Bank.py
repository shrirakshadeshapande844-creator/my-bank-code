bal = 100000
withdrawal =True

while withdrawal:
    amount = int(input("Enter your amount"))
    if amount<= bal:
        print("amount Debited")
        bal = bal - amount
        print("your current balance is:",bal)
    else:
        print("Insufficient balance")
    choice = input("do you want to withdrawal again")
    if choice.lower() == "yes":
        withdrawal = True
    elif choice.lower() == "No":
        withdrawal = False
        print("thank you! Exiting")
    else:
        print("Invalid option, Exiting program")
        withdrawal = False

