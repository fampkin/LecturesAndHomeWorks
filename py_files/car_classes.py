class Car():
    def __init__(self, mark, model, year, color):
        self.mark = mark
        self.model = model
        self.year = year
        self.color = color
    def print_car_info(self):
        print(f"Марка: {self.mark}\n"
              f"Модель: {self.model}\n"
              f"Год: {self.year}\n"
              f"Цвет: {self.color}")
    def is_match(self, search_mark):
        return self.mark.lower() == search_mark.lower()

class LightCar(Car):
    def __init__(self, mark, model, year, color, body_type, count_seats):
        super().__init__(mark, model, year, color)
        self.body_type = body_type
        self.count_seats = count_seats
    def print_car_info(self):
        super().print_car_info()
        print(f"Тип кузова: {self.body_type}\n"
              f"Количество мест: {self.count_seats}\n")

class Truck(Car):
    def __init__(self, mark, model, year, color, max_load, body_volume):
        super().__init__(mark, model, year, color)
        self.max_load = max_load
        self.body_volume = body_volume
    def print_car_info(self):
        super().print_car_info()
        print(f"Максимальная нагрузка: {self.max_load}\n"
              f"Объем кузова: {self.body_volume}\n")

class Bus(Car):
    def __init__(self, mark, model, year, color, count_seats):
        super().__init__(mark, model, year, color)
        self.count_seats = count_seats
    def print_car_info(self):
        super().print_car_info()
        print(f"Количество мест: {self.count_seats}\n")

# Создаем список автомобилей
cars = [
    LightCar("Toyota", "Corolla", 2020, "Red", "Sedan", 5),
    Truck("Volvo", "S60", 2010, "Blue", 25000, 150),
    Bus("Mercedes-Benz", "Tourismo", 2021, "White", 45),
    LightCar("BMW", "X5", 2019, "Black", "SUV", 5),
    Truck("MAN", "TGX", 2018, "Red", 40000, 200)
]

# Выводим информацию о всех автомобилях
print("=== Информация о всех автомобилях ===")
for car in cars:
    car.print_car_info()
    print("-" * 30)

# Поиск автомобилей по марке
search_mark = input("\nВведите марку автомобиля для поиска: ")
print(f"\n=== Результаты поиска по марке '{search_mark}' ===")
found = False
for car in cars:
    if car.is_match(search_mark):
        car.print_car_info()
        print("-" * 30)
        found = True

if not found:
    print(f"Автомобили марки '{search_mark}' не найдены.") 