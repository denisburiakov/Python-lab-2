def longer_str(n, lst):
    max_symb = 0
    for i in range(n):
        count = len(lst[i])
        if count > max_symb:
            max_symb = count
    return max_symb

words = ["rek", "nine", "ghjkfjdhsgfhjsd"]
N = len(words)
longest = longer_str(N, words)
print(f"Longest word in list: {longest}")