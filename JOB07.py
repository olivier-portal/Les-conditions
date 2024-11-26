rows = 10
ascii_value = 97

for i in range(rows):
    for j in range(i+1):
        alphabet = chr(ascii_value)
        ascii_value += 1
    print()