"""
If we list all the natural numbers below 10 that are multiples 
of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""
from functools import reduce
import sys


def sum_of_multiples(n: int) -> int:
    return reduce(lambda x, y: x + y,
                  [i for i in range(0, n)
                   if i % 3 == 0 or i % 5 == 0])


# get n
n = abs(int(sys.argv[1])) if len(sys.argv) == 2 and sys.argv[1].isdigit() else 1000

# n = 10 => 23
# n = 1000 => 233168
print(sum_of_multiples(n))
