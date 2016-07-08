# Sum of primes below n

def isprime(n):
    # Returns true if n is prime
    if n == 2:
        return True
    if n == 3:
        return True
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True

def sumofprimes(n):
    i = 2
    sum = 0
    while i < n:
        if isprime(i):
            sum += i
            i += 1
        else:
            i += 1
    print sum
    return sum

sumofprimes(2000000)