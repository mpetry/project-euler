# Find largest prime factor of a number n

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

# Check prime factors of n

i = 2
largestPrimeFactor = 1
n = 600851475143

while i <= n:
    if (n % i == 0) and (isprime(i) == True):
        largestPrimeFactor = i
        print i
        i += 1
    else:
        i += 1

print largestPrimeFactor
