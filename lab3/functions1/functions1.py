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


#6
