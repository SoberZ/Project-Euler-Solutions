#!/usr/bin/python3

sum = 0
n1, n2 = 1, 2
# file = open("nrs.txt", "w+")

while n1 < 4000000 or n2 < 4000000:
    # file.write("{0:d} ".format(n1))

    if n1 % 2 == 0:
        sum += n1

    n1, n2 = n2, n1 + n2

print(sum)