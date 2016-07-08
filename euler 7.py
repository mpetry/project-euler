# Code to find the nth prime

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

def nthprime(n):
    count = 1
    i = 2
    while count <= n:
        if isprime(i):
            count += 1
            candidate = i
            i += 1
        else:
            i += 1
    return candidate

print nthprime(10001)
