import random
import string

length = int(input("Enter password length (Minimum 4): "))

if length < 4:
    print("Password length should be at least 4.")
else:
    password = [
        random.choice(string.ascii_uppercase),
        random.choice(string.ascii_lowercase),
        random.choice(string.digits),
        random.choice(string.punctuation)
    ]

    all_characters = (
        string.ascii_letters +
        string.digits +
        string.punctuation
    )

    for i in range(length - 4):
        password.append(random.choice(all_characters))

    random.shuffle(password)

    print("\nStrong Password:")
    print("".join(password))