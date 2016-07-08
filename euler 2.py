# Find sum of even fibonaccis less than four million

fib = 1
prevFib = 1
sum = 0

while fib < 4000000:
    if fib%2 == 0:
        sum += fib
        print fib
        fibTemp = fib
        fib = fib + prevFib
        prevFib = fibTemp
    else:
        fibTemp = fib
        fib = fib + prevFib
        prevFib = fibTemp

print sum