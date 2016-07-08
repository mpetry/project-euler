# Find sum of multiples of 3 and 5 that are less than 1000

sum = 0
n= 0

while n < 1000:
    if (n%3 == 0) or (n%5 == 0):
        print n
        sum += n
        n += 1
    else:
        n+=1
print sum

