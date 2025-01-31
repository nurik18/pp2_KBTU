# Создание и доступ к кортежам
tupleData = (10, 20, 30, 40, 50)
print("Исходный кортеж:", tupleData)
print("Первый элемент:", tupleData[0])
print("Последний элемент:", tupleData[-1])

# Обновление кортежей (неизменяемость и обходное решение)
tupleList = list(tupleData)
tupleList[1] = 25
tupleData = tuple(tupleList)
print("Кортеж после изменения второго элемента:", tupleData)

# Распаковка кортежа
a, b, c, d, e = tupleData
print("Распакованные значения:", a, b, c, d, e)

# Перебор кортежа
for item in tupleData:
    print("Элемент кортежа:", item)

# Объединение кортежей
tupleExtra = (60, 70, 80)
combinedTuple = tupleData + tupleExtra
print("Объединенный кортеж:", combinedTuple)

# Методы кортежей
print("Количество элементов '25' в кортеже:", tupleData.count(25))
print("Индекс элемента '40':", tupleData.index(40))

# Практическое упражнение: нахождение максимального числа
maxNumber = max(tupleData)
print("Максимальное число в кортеже:", maxNumber)
