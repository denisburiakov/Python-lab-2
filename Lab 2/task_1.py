def sun(n):
    total = 0
    for i in range(1, n + 1):
        if i % 2 == 0:
            total += i
    return total

N = int(input("Enter number N: "))
result = sun(N)
print(f"Сумма всех чётных чисел от 1 до {N} равна: {result}")