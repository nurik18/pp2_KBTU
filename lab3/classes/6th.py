numbers = [10, 15, 17, 23, 25, 29, 31, 37, 40, 41]

prime_numbers = [x for x in numbers if(lambda n: n > 1 and all(n % i != 0 for i in range(2, int(n ** 0.5) + 1)))(x)]

print("Prime numbers:", prime_numbers)