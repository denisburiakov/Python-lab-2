def fibonacci_up_to_n(n):
    if n < 0:
        return []

    fib_sequence = []
    a, b = 0, 1

    while a <= n:
        fib_sequence.append(a)
        a, b = b, a + b

    return fib_sequence


# Ввод данных
try:
    N = int(input("Введите число N: "))
    result = fibonacci_up_to_n(N)
    print(f"Числа Фибоначчи до {N}: {result}")
except ValueError:
    print("Ошибка: введите целое число!")