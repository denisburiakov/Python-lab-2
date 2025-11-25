def dictionarysq(n):
    squares = {}
    for i in range(1, n+1):
        squares[i] = i * i
    return squares

N = int(input("Enter N: "))
squares_dict = dictionarysq(N)
print(squares_dict)