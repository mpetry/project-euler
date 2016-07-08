# Code to find largest palindrome

def isPalindrome(word):
    if list(word) == list(reversed(word)):
        return True
    else:
        return False

largest = 0

for i in range(100, 999):
    for j in range(100, 999):
        if isPalindrome(str(i * j)) and (i * j) > largest:
            largest = i * j
            j += 1
            print largest
        else:
            j += 1
    i += 1

print largest