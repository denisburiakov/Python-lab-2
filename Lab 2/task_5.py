def three(n, lst):
    result = []
    for i in range(0, n):
        if lst[i] % 3 == 0:
            result.append(lst[i])
    return result


numbers = [81, 2, 6, 9, 18, 21, 34, 54, 76]
N = len(numbers)
res = three(N, numbers)
print(f"Numbers 3: {res} ")
