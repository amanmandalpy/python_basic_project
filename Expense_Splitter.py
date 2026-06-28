def expense_splitter():

    people = {}

    n = int(input("Enter number of people: "))

    print()

    # Input names and expenses
    for i in range(n):
        name = input(f"Enter name of Person {i+1}: ")
        amount = float(input(f"How much did {name} pay? ₹"))
        print()

        people[name] = amount

    total_expense = sum(people.values())
    share = total_expense / n

    print("\n" + "=" * 50)
    print(f"Total Expense : ₹{total_expense:.2f}")
    print(f"Each Person Should Pay : ₹{share:.2f}")
    print("=" * 50)

    print("\nSettlement\n")

    for name, paid in people.items():

        difference = paid - share

        if difference > 0:
            print(f"{name} should RECEIVE ₹{difference:.2f}")

        elif difference < 0:
            print(f"{name} should PAY ₹{abs(difference):.2f}")

        else:
            print(f"{name} is SETTLED ✅")


expense_splitter()