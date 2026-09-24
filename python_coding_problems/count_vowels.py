vowels = ("a", "e", "i", "o", "u")

text = input("Enter your text: ")
def count_vowels(text):
    count = 0
    for char in text.lower():
        if char in vowels:
            count +=1
    return count

print(count_vowels(text))
