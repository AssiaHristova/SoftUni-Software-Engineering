def numbers_searching(*args):
    numbers = [int(el) for el in args]
    sorted_numbers = sorted(numbers)
    duplicates = []
    missing_number = 0

    for i in range(len(sorted_numbers) - 1):
        if sorted_numbers[i] == sorted_numbers[i + 1]:
            duplicate = sorted_numbers[i + 1]
            duplicates.append(duplicate)

    for el in duplicates:
        sorted_numbers.remove(el)

    duplicates_set = set(duplicates)

    for j in range(min(sorted_numbers), max(sorted_numbers) + 1):
        if j not in sorted_numbers:
            missing_number = j
            break
    return [missing_number, sorted(duplicates_set)]


print(numbers_searching(1, 2, 4, 2, 5, 4))
print(numbers_searching(5, 5, 9, 10, 7, 8, 7, 9))
print(numbers_searching(50, 50, 47, 47, 48, 45, 49, 44, 47, 45, 44, 44, 48, 44, 48))
