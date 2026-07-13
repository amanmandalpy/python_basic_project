import time

phrase = "Python is the best coding language"
word_count = len(phrase.split())
print("press enter to start.")

start_time = time.time()
attempt = input("Now type the phrase here: ")
end_time = time.time()

time_taken = (end_time - start_time) / 60
wpm = round(word_count / time_taken, 2)

if attempt == phrase:
    print(f"Congratulations! Your typing speed is {wpm} WPM.")
else:
    print("Try again. You didn't type the phrase correctly.")


# import time

# print("===== Typing Speed Test =====")
# input("Press Enter to start...")

# start_time = time.time()

# text = input("Start typing:\n")

# end_time = time.time()

# # Time in minutes
# time_taken = (end_time - start_time) / 60

# # Count words typed by user
# word_count = len(text.split())

# # Calculate WPM
# if time_taken > 0:
#     wpm = round(word_count / time_taken, 2)
# else:
#     wpm = 0

# print("\n===== Result =====")
# print(f"Words Typed : {word_count}")
# print(f"Time Taken  : {round((end_time - start_time), 2)} seconds")
# print(f"Typing Speed: {wpm} WPM")

