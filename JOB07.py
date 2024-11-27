word = "abcdefghijklmnopqrstuvwxyz"*10
length = len(word)
i = 1

while i <= length:
    line = word[:i]
    i += 2
    print(line)