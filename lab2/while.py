# Программа с циклом while

# Цикл while с условием
count = 1
while count <= 5:
    print("Число:", count)
    count += 1

# Бесконечный цикл с возможностью выхода
while True:
    user_input = input("Введите 'стоп' для выхода: ")
    if user_input.lower() == "стоп":
        print("Цикл завершен.")
        break
    print("Вы ввели:", user_input)

# Проверка пароля с ограничением попыток
correct_password = "1234"
attempts = 3

while attempts > 0:
    password = input("Введите пароль: ")
    if password == correct_password:
        print("Доступ разрешен!")
        break
    else:
        attempts -= 1
        print(f"Неверный пароль. Осталось попыток: {attempts}")
else:
    print("Доступ заблокирован.")
