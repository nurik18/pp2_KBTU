# 1
def grammToOunces(grams):
    return 28.3495231 * grams

sugar = grammToOunces(500)
print(f"\nСахар нужен {sugar} унций\n")


# 2
def fahrenheitToCelsius(F):
    return (5 / 9) * (F - 32)

almaty = fahrenheitToCelsius(432)
print(f"В Алматы сейчас солнечно, {almaty} градус по цельсию\n")


# 3
def solve(numheads, numlegs):
    heads = numheads
    legs = numlegs

    for chickens in range(1, heads+1):
        rabbits = heads - chickens
        if 2 * chickens + 4 * rabbits == legs:
            print(f"Кур: {chickens}\nЗайцев:{rabbits}\n")
            break

solve(35,94)

# 4
s = '2 4 5 6 7 8 9 11 12 23 27 30'
def filterPrime(s):
    numList = [int(i) for i in s.split()]
    prime_numbers = [x for x in numList if(lambda n: n > 1 and all(n % i != 0 for i in range(2, int(n ** 0.5) + 1)))(x)]
    return prime_numbers

print(filterPrime(s))
print()
 

#5
# s = str(input("Введите символы (без пробелов): "))
s = 'abc'
def permutate(s, p = ''):
    if len(s) == 0:
        print(p, end = ' ')
        return
    for i in range(len(s)):
        t = s[:i]+s[i+1:]
        permutate(t, p + s[i])

                
permutate(s)
print()
print()


#6
s = 'We are ready'
def reverseString(s):
    l = [str(i) for i in s.split()]
    for i in range(len(l)-1, -1, -1):
        print(l[i], end = " ")

reverseString(s)
print("\n")


#7
def has_33(nums):
    for i in range(1, len(nums)):
        if nums[i] == nums[i-1] == 3:
            print("True")
            return
    print("False")
    return 

has_33([1, 3, 3])
has_33([1, 3, 1, 3]) 
has_33([3, 1, 3]) 

print()


#8
def spy_game(nums):
    l = []
    for i in nums:
        if i == 0 or i == 7:
            l.append(i)
    
    for i in range(2, len(l)):
        if l[i-2] == l[i-1] == 0 and l[i] == 7:
            print("True")
            return
    print("False")
    return

spy_game([1,2,4,0,0,7,5]) 
spy_game([1,0,2,4,0,5,7])  
spy_game([1,7,2,0,4,5,0]) 
print()


#9
import math

def sphere_volume(radius):
    return (4/3) * math.pi * radius**3

r = 5
print(f"The volume of a sphere with radius {r} is {sphere_volume(r):.2f}\n")


#10
l = [1, 2, 1 , 2, 3 , 4 , 5 , 6, 4, 5 , 3, 6, 10]
def uniqueL(l):
    nl = []
    nl.append(l[0])
    for i in range(len(l)):
        f = False
        for j in range(len(nl)):
            if l[i] == nl[j]:
                f = True
                break
        if f == False:
            nl.append(l[i])

    print(nl)

uniqueL(l)
print()


#11
def isPalindrome(s):
    s = ''.join(c.lower() for c in s if c.isalnum())
    return s == s[::-1]

print(isPalindrome("madam"))
print()


#12
l = [4,9,7]
def histogram(l):
    for i in l:
        print("*"*i)

histogram(l)
print()


#13
import random
def play():
    c = 1
    name = str(input("Hello! What's your name?\n"))
    n = random.randint(1,20)
    number = int(input(f"Well, {name}, I am thinking of a number between 1 and 20.\nTake a guess.\n"))
    while number != n:
        c += 1
        if number < n:
            number = int(input("Your guess is too low.\nTake a guess\n"))
        elif number > n:
            number = int(input("Your guess is too high.\nTake a guess\n"))

    print(f"Good job, {name}! You guessed my number in {c} guesses!")

play()
print()

