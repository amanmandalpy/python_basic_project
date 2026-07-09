class ATM:

    # Constructor
    def __init__(self):
        self.balance = 5000

    # Check Balance
    def check_balance(self):
        print("\n---------------------------")
        print(f"Current Balance : ₹{self.balance}")
        print("---------------------------")

    # Deposit Money
    def deposit(self):
        amount = float(input("Enter amount to deposit: ₹"))

        if amount > 0:
            self.balance += amount
            print(f"₹{amount} deposited successfully.")
            print(f"Available Balance: ₹{self.balance}")
        else:
            print("Invalid Amount!")

    # Withdraw Money
    def withdraw(self):
        amount = float(input("Enter amount to withdraw: ₹"))

        if amount <= 0:
            print("Invalid Amount!")

        elif amount > self.balance:
            print("Insufficient Balance!")

        else:
            self.balance -= amount
            print(f"₹{amount} withdrawn successfully.")
            print(f"Available Balance: ₹{self.balance}")

    # Main Menu
    def menu(self):

        while True:

            print("\n==============================")
            print("       ATM MACHINE")
            print("==============================")
            print("1. Check Balance")
            print("2. Deposit Money")
            print("3. Withdraw Money")
            print("4. Exit")

            choice = input("Enter your choice (1-4): ")

            if choice == "1":
                self.check_balance()

            elif choice == "2":
                self.deposit()

            elif choice == "3":
                self.withdraw()

            elif choice == "4":
                print("\nThank you for using ATM.")
                break

            else:
                print("Invalid Choice! Please try again.")


# Create Object
atm = ATM()

# Start ATM
atm.menu()