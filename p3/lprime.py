import math

number = 600851475143
arr = []
maxPrime = -1

while number % 2 == 0:
    maxPrime = 2
    number >>= 1

for i in range(3, int(math.sqrt(number) + 1), 2):
    while number % i == 0:
        maxPrime = i
        number = number / i

if number > 2:
    maxPrime = number

print(maxPrime)