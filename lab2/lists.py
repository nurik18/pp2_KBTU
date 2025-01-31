# Создание списка
numbersList = [10, 20, 30, 40, 50]
print("Исходный список:", numbersList)

# Доступ к элементам списка
print("Первый элемент:", numbersList[0])
print("Последний элемент:", numbersList[-1])

# Изменение элемента списка
numbersList[1] = 25
print("Список после изменения второго элемента:", numbersList)

# Добавление элемента
numbersList.append(60)
numbersList.insert(2, 35)
print("Список после добавления элементов:", numbersList)

# Удаление элемента
numbersList.remove(30)
deletedItem = numbersList.pop()
print("Список после удаления элементов:", numbersList)
print("Удаленный элемент:", deletedItem)

# Перебор элементов списка
for number in numbersList:
    print("Элемент списка:", number)

# Генератор списка
squaredList = [x ** 2 for x in numbersList]
print("Список квадратов:", squaredList)

# Сортировка списка
numbersList.sort()
print("Отсортированный список:", numbersList)

# Копирование списка
copiedList = numbersList.copy()
print("Копия списка:", copiedList)

# Объединение списков
anotherList = [70, 80, 90]
combinedList = numbersList + anotherList
print("Объединенный список:", combinedList)

# Методы списка
print("Длина списка:", len(numbersList))
print("Количество элементов '25' в списке:", numbersList.count(25))

# Практическое упражнение: нахождение максимального числа
maxNumber = max(numbersList)
print("Максимальное число в списке:", maxNumber)
