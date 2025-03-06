import time

# 1
numbers = [1,2,3,4,5,6,7]
def multiplyAll(n) :
    total = 1
    for i in range(len(n)):
        total *= n[i]

    return total

print(multiplyAll(numbers))

# 2

text = "HihIhAHa"
def calculateLetters(s):
    upperCount = 0
    lowerCount = 0
    for i in text:
        if i.isupper():
            upperCount += 1
        elif i.islower():
            lowerCount += 1
        else:
            return None
    print(f'Upper:{upperCount}\nLower:{lowerCount}')
calculateLetters(text)
# 3
def palindromeChecker(s):
     if s == s[::-1]:
         return "True"
     else:
         return "False"
     
text = 'aboba' 
print(f'{text} is palindrome: {palindromeChecker(text)}')
text = 'qazaq'
print(f'{text} is palindrome: {palindromeChecker(text)}')
text = 'orys'
print(f'{text} is palindrome: {palindromeChecker(text)}')

# 4 
n = 25100
ms = 2123.0
time.sleep(ms/1000)
total = 25100**0.5
print(f'sqrt of {n} after {int(ms)}ms is {total}')

# 5
l = (1,2,3)
flag = all(l)
print(f'{l} is {flag}')
l = (0,1,2)
print(f'{l} is {flag}')
#hehe
#haha
#hoho
