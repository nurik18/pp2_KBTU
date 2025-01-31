# Программа с циклом for

# Перебор элементов списка
fruits = ["яблоко", "банан", "вишня"]
for fruit in fruits:
    print("Фрукт:", fruit)

# Перебор чисел с использованием range
for i in range(1, 6):
    print("Число:", i)

# Перебор строки
word = "Python"
for letter in word:
    print("Буква:", letter)

# Вложенный цикл
for i in range(1, 4):
    for j in range(1, 4):
        print(f"i={i}, j={j}")

# Использование break и continue
for number in range(1, 10):
    if number == 5:
        print("Прерывание цикла при числе 5")
        break
    if number % 2 == 0:
        continue
    print("Нечетное число:", number)
