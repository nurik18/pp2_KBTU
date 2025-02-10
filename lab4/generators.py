number = 36
number = int(number ** 0.5) + 1
n = [int(i**2) for i in range(number)]
print(n)
print()

# --------------

# number = int(input("Введите число: "))
number = 9
n = [int(i) for i in range(0,number+1,2)]
print(n)
print()

# --------------

n = 48
def customIterator(n):
    l = [i for i in range(n) if i % 3 == 0 and i % 4 == 0]
    return l
print(customIterator(n))
print()

# --------------

# a = int(input("Vvedite a: "))
# b = int(input("Vvedite b: "))
a = 0
b = 10

squares = [int (i**2) for i in range(a, b)]
print(squares)
print()

# --------------

n = 10

rev = [int(i) for i in range(n, -1, -1)]
print(rev)