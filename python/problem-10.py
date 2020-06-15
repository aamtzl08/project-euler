def primes_below_n(n):
    primes = [2, 3]
    suma = 5
    number = 5
    while number < n:
        prime = True
        bound = round(number ** 1/2)
        for i in primes:
            if i > bound:
                break
            elif number % i == 0:
                prime = False
                break
        if prime:
            suma += number
            primes.append(number)
        number += 2
    return suma
print(primes_below_n(2000000))