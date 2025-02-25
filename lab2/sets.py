# Создаем два множества
set1 = {"яблоко", "банан", "вишня"}
set2 = {"апельсин", "киви", "банан"}

# Доступ к элементам множества (перебор)
print("Элементы множества set1:")
for item in set1:
    print(item)

# Добавление элементов
set1.add("груша")
print("\nПосле добавления груши в set1:", set1)

# Удаление элементов
set1.remove("банан")  # вызовет ошибку, если элемента нет
print("\nПосле удаления банана из set1:", set1)

# Другой способ удаления (без ошибки, если элемента нет)
set1.discard("вишня")
print("\nПосле удаления вишни из set1:", set1)

# Объединение множеств
set3 = set1.union(set2)
print("\nОбъединенное множество set3:", set3)

# Использование методов множеств
print("\nПересечение set1 и set2:", set1.intersection(set2))
print("Разница set1 и set2:", set1.difference(set2))
print("Симметричная разница set1 и set2:", set1.symmetric_difference(set2))

# Упражнение: пользователь вводит элементы, добавляем их в множество
user_set = set()
print("\nВведите 3 элемента для множества:")
for _ in range(3):
    user_set.add(input("Введите элемент: "))

print("\nВаше множество:", user_set)
