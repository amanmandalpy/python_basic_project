def find_s_l_n(numbers):

    unique_numbers = list(set(numbers))

    if len(unique_numbers) < 2:
        return "there is no unique second largest number"

    unique_numbers.sort()

    return unique_numbers[-2]


num = [10, 25, 8, 40, 30]
print(f"the second largest number is: {find_s_l_n(num)}")