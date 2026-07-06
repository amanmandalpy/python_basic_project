from datetime import datetime

dob = input("Enter your Date of Birth (DD-MM-YYYY): ")

birth_date = datetime.strptime(dob, "%d-%m-%Y").date()
today = datetime.today().date()

years = today.year - birth_date.year
months = today.month - birth_date.month
days = today.day - birth_date.day

if days < 0:
    months -= 1
    days += 30  # Simple approximation

if months < 0:
    years -= 1
    months += 12

print("\n------ Age Details ------")
print("Years :", years)
print("Months:", months)
print("Days  :", days)