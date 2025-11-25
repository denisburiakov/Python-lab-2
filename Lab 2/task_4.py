def isPalindrome(x):
    return str(x) == str(x)[::-1]

x = input()
print(isPalindrome(x))