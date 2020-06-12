# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

# What is the 10 001st prime number?
def n_prime(n):
    primes = [2, 3]
    number = 4
    while len(primes) < n:
        prime = True
        bound = round(number ** 1/2)
        for i in primes:
            if i > bound:
                break
            elif number % i == 0:
                prime = False
                break
        if prime:
            primes.append(number)
        number +=1
    return primes

print(n_prime(10001)[-1])