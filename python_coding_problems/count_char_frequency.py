# text = "python"
# char_count ={}

# for char in text:
#     if char in char_count:
#         char_count[char] +=1

#     else:
#         char_count[char] = 1

# for char, count in char_count.items():
#     print(f"'{char}': {count}")

from collections import Counter


input_string = input("Enter a string: ")


char_counts = Counter(input_string)

for char, count in char_counts.items():
    print(f"'{char}': {count}")