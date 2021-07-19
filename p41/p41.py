from math import sqrt
from itertools import count, islice

def is_prime(n):
    return n > 1 and all(n % i for i in islice(count(2), int(sqrt(n)-1)))

def isPrime(n):
  if n <= 3:
    return n > 1
  elif n % 2 == 0 or n % 3 == 0:
    return False
  return True

def all_perms(elements):
    if len(elements) <= 1:
        yield elements  # Only permutation possible = no permutation
    else:
        # Iteration over the first element in the result permutation:
        for (index, first_elmt) in enumerate(elements):
            other_elmts = elements[:index]+elements[index+1:]
            for permutation in all_perms(other_elmts):
                yield [first_elmt] + permutation


lists = []
for nNumbers in range(1, 10):
  l = []
  for n in range(1, nNumbers+1):
    l.append(n)
  lists.append(l)

highest = 0
for li in lists:
  # Create permutations for list
  perms = list(all_perms(li))

  # Check every permutation for a list
  for perm in perms:
    num = int(''.join(map(str, perm)))
    if isPrime(num) and num > highest:
      highest = num

print(highest)
