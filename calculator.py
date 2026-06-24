import math

def calculator():
    while True:
        print("\n===== Python Calculator =====")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Power")
        print("6. Square Root")
        print("7. Percentage")
        print("8. Exit")

        choice = input("Choose an option: ")

        try:
            if choice == "1":
                a = float(input("First number: "))
                b = float(input("Second number: "))
                print("Result:", a + b)

            elif choice == "2":
                a = float(input("First number: "))
                b = float(input("Second number: "))
                print("Result:", a - b)

            elif choice == "3":
                a = float(input("First number: "))
                b = float(input("Second number: "))
                print("Result:", a * b)

            elif choice == "4":
                a = float(input("First number: "))
                b = float(input("Second number: "))
                if b == 0:
                    print("Cannot divide by zero!")
                else:
                    print("Result:", a / b)

            elif choice == "5":
                a = float(input("Base: "))
                b = float(input("Exponent: "))
                print("Result:", a ** b)

            elif choice == "6":
                a = float(input("Number: "))
                if a < 0:
                    print("Cannot find square root of a negative number!")
                else:
                    print("Result:", math.sqrt(a))

            elif choice == "7":
                amount = float(input("Amount: "))
                percent = float(input("Percentage: "))
                print("Result:", (amount * percent) / 100)

            elif choice == "8":
                print("Goodbye!")
                break

            else:
                print("Invalid option!")

        except ValueError:
            print("Please enter valid numbers!")

calculator()