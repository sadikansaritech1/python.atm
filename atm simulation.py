

balance = 10000

while True:
    print("\n--- Banking Simulation ---")
    print("1. Withdraw")
    print("2. Deposit")
    print("3. Check Balance")
    print("4. Exit")
    
    choice = input("Enter choice (1/2/3/4): ")
    
    if choice == "1":
        amount = float(input("Enter withdrawal amount: "))
        if amount > balance:
            print("Insufficient balance!")
        elif amount <= 0:
            print("Amount must be positive!")
        else:
            balance -= amount
            print(f"Withdrawn: {amount}")
            print(f"Current balance: {balance}")
    
    elif choice == "2":
        amount = float(input("Enter deposit amount: "))
        if amount <= 0:
            print("Amount must be positive!")
        else:
            balance += amount
            print(f"Deposited: {amount}")
            print(f"Current balance: {balance}")
    
    elif choice == "3":
        print(f"Current balance: {balance}")
    
    elif choice == "4":
        print("Thank you for using our bank!")
        break
    
    else:
        print("Invalid choice! Please try again.")

 