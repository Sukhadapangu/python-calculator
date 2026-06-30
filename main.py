# ===========================
#     SIMPLE CALCULATOR
# ===========================

print("=" * 30)
print("   SIMPLE CALCULATOR")
print("=" * 30)

while True:

    print("\nChoose an operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

    # Take user's choice
    choice = input("\nEnter your choice (1-5): ")

    # Exit the calculator
    if choice == "5":
        print("\nThank you for using the calculator!")
        break

    # Check if the choice is valid
    if choice in ("1", "2", "3", "4"):

        # Take two numbers
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        # Perform the selected operation
        if choice == "1":
            result = num1 + num2
            print(f"\nResult = {result}")

        elif choice == "2":
            result = num1 - num2
            print(f"\nResult = {result}")

        elif choice == "3":
            result = num1 * num2
            print(f"\nResult = {result}")

        elif choice == "4":
            if num2 == 0:
                print("\nError! Division by zero is not allowed.")
            else:
                result = num1 / num2
                print(f"\nResult = {result}")

    else:
        print("\nInvalid choice! Please enter a number between 1 and 5.")
