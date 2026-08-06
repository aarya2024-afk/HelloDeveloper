balance = 0

while True:
    print("\n====== SIMPLE BANKING SYSTEM ======")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        amount = float(input("Enter amount to deposit: ₹"))
        if amount > 0:
            balance += amount
            print(f"₹{amount:.2f} deposited successfully.")
        else:
            print("Invalid amount!")

    elif choice == "2":
        amount = float(input("Enter amount to withdraw: ₹"))
        if amount <= 0:
            print("Invalid amount!")
        elif amount > balance:
            print("Insufficient Balance!")
        else:
            balance -= amount
            print(f"₹{amount:.2f} withdrawn successfully.")

    elif choice == "3":
        print(f"Current Balance: ₹{balance:.2f}")

    elif choice == "4":
        print("Thank you for using the Banking System.")
        break

    else:
        print("Invalid choice! Please try again.")