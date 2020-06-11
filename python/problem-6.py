# The sum of the squares of the first ten natural numbers is 1 + 4 + ... + 100 = 385
# The square of the sum is  (1+2+...+3) ^ 2 = 3025
# The difference is 3025 - 385
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
# Sum of a series from 1 to n by math
def sum_of_series(bound):
    return (bound * (bound + 1)) // 2
# Sum of squeres by math
def sum_squares_math(bound):
    return (2 * bound + 1) * (bound + 1) * bound // 6

# Sum of squares by brute force
def sum_squares(bound):
    suma = 0
    for i in range(1, bound + 1):
        suma += i ** 2
    return suma

print(sum_squares_math(100) - sum_of_series(100) ** 2)