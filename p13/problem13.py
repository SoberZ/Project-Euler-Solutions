sum = 0

with open("numbers.txt") as file:
    for line in file:
        line = line.rstrip()
        if line:
            sum = sum + int(line)
    print(str(sum)[:10])
