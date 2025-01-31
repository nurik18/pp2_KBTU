age = int(input("Введите ваш возраст: "))

isAdult = age >= 18 

if isAdult:
    print("Доступ разрешен.")
else:
    print("Доступ запрещен.")

isRaining = True
haveUmbrella = False

if isRaining and not haveUmbrella:
    print("Возьмите зонт!")
else:
    print("Можно идти без зонта.")
