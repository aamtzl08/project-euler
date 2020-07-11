# What is the index of the first term in the Fibonacci sequence to contain 1000 digits?

# Helper function to calculate the nth fibonacci number
fib_dict = {1: 1, 2:1}
def fib(n, d):
    if n in d:
        return d[n]
    else:
        ans = fib(n-1,d) + fib(n-2, d)
        d[n] = ans
        return ans



n = 0
fib_number = '0'

# Loop for searching the n index 
while len(fib_number) < 1000:
    n += 1
    fib_number = str(fib(n, fib_dict))
    if n > 2:
        fib_dict[n] = int(fib_number)

print(n) # Answer 4782
