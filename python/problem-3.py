# The prime factors of 13195 are 5, 7, 13 and 29.

# What is the largest prime factor of the number 600851475143 ?

def prime_factorization(number):
    if number > 1:
        primes = []
        divisor = 2
        actual = number
        while actual != 1:
            if actual % divisor == 0:
                actual = actual / divisor
                if divisor not in primes:
                    primes.append(divisor)
            else:
                divisor += 1    
            
        return primes
    
    else:
        return 1

print(prime_factorization(600851475143))