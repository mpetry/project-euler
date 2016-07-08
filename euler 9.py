# Solve for pythagorean triplet a + b + c = n

def ispythag(a, b, c):
    if (a * a + b * b) == (c * c):
        return True
    else:
        return False

def correctsum(a, b, c, n):
    if (a+b+c) == n:
        return True
    else:
        return False

def findproduct(n):
    for a in range(1, n):
        for b in range(1, n):
            for c in range(1, n):
                if ispythag(a, b, c):
                    if correctsum(a,b,c, n):
                        print a
                        print b
                        print c
                        print a*b*c
                        return a*b*c
                c += 1
            b += 1
        a += 1

findproduct(1000)