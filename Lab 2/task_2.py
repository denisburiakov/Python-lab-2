def remove_duplicates(lst):
    return list(set(lst))

numbers = [1, 2, 2, 3, 4, 4, 5, 1, 6]
result = remove_duplicates(numbers)
print(f"Исходный список: {numbers}")
print(f"Список без дубликатов: {result}")