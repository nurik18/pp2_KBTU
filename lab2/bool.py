age = int(input("Введите ваш возраст: "))

is_adult = age >= 18  # Булево значение

if is_adult:
    print("Доступ разрешен.")
else:
    print("Доступ запрещен.")

# Булевы значения в операциях
is_raining = True
have_umbrella = False

if is_raining and not have_umbrella:
    print("Возьмите зонт!")
else:
    print("Можно идти без зонта.")
