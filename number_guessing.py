import random

def guess_the_number():
    
    secret_number = random.randint(1, 100)
    attempts = 0
    
    print("Welcome to the Guessing Game!")
    print("I am thinking of a number between 1 and 100.")

    
    while True:
        user_input = input("Enter your guess: ")
        
        if not user_input.isdigit():
            print("Please enter a valid whole number.")
            continue
            
        guess = int(user_input)
        attempts += 1

        # 3. Evaluate the user's guess against the secret target
        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            print(f" Correct! You found the number in {attempts} attempts.")
            break 


guess_the_number()
