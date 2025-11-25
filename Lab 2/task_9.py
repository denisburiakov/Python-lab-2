def set_operations(set1, set2):
    union_set = set1 | set2
    intersection_set = set1 & set2

    return union_set, intersection_set


A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

union, intersection = set_operations(A, B)

print(f"Множество A: {A}")
print(f"Множество B: {B}")
print(f"Объединение: {union}")
print(f"Пересечение: {intersection}")