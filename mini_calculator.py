while True:
    print("\n========== MINI CALCULATOR ==========")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Modulus")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == "6":
        print("Thank you for using the calculator!")
        break

    if choice not in ["1", "2", "3", "4", "5"]:
        print("Invalid choice! Please try again.")
        continue

    num1 = float(input("Enter First Number: "))
    num2 = float(input("Enter Second Number: "))

    if choice == "1":
        print("Result =", num1 + num2)

    elif choice == "2":
        print("Result =", num1 - num2)

    elif choice == "3":
        print("Result =", num1 * num2)

    elif choice == "4":
        if num2 == 0:
            print("Error: Division by zero is not allowed.")
        else:
            print("Result =", num1 / num2)

    elif choice == "5":
        if num2 == 0:
            print("Error: Modulus by zero is not allowed.")
        else:
            print("Result =", num1 % num2)