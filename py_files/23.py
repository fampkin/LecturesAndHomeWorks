import re

def validate_filename():
    try:
        filename = input("Введите имя файла: ")
        if re.search(r'[<>:"/\\|?*]', filename):
            raise ValueError("Недопустимое имя файла")
        print("Имя файла введено корректно")
    except ValueError as e:
        print(e)

def validate_birth_date():
    try:
        birth_date = input("Введите дату рождения (дд.мм.гггг): ")
        if not re.match(r'^\d{2}\.\d{2}\.\d{4}$', birth_date):
            raise ValueError("Неверный формат даты")
        print("Дата введена корректно")
    except ValueError as e:
        print(e)

def validate_coordinates():
    try:
        coords = input("Введите координаты точки на плоскости (x, y): ")
        x, y = coords.split(',')
        x = float(x.strip())
        y = float(y.strip())
        print("Координаты введены корректно")
    except ValueError:
        print("Некорректные координаты")

validate_filename()
validate_birth_date()
validate_coordinates()
