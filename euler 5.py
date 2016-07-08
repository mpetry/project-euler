# Smallest number n divisible by all integers from 1-20

def divisible(n, k): # Function for determining if n is divisible by all ints from 1 to k, inclusive
    i = 1
    div = False
    while i <= k:
        if n % i == 0:
            div = True
            i += 1
        else:
            div = False
            break
    return div

n = 1
k = 20
allDivisible = False

while ~allDivisible:
    if divisible(n, k):
        allDivisible = True
        break
    else:
        n += 1

print n



