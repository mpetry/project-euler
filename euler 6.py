# Code to find difference between sum of squares and square of sum of n

def sumOfSquares(n):
    i = 0
    sum = 0
    while i <= n:
        sum += (i * i)
        i += 1
    return sum

def squareOfSums(n):
    i = 0
    sum = 0
    while i <= n:
        sum += i
        i += 1
    return (sum * sum)

print (squareOfSums(100) - sumOfSquares(100))
