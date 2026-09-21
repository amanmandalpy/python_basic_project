def remove_dup_num(numbers):

    seen = set()
    result  = []

    for number in numbers:
        if number not in seen:
            seen.add(number)
            result.append(number)

    return result
numbers = [4,2,4,1,2,5,1]
print(remove_dup_num(numbers))