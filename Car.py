class Car:

    def __init__(self, model, year, engine_capacity, price, mileage):
        self.model = model
        self.year = year
        self.engine_capacity = engine_capacity
        self.price = price
        self.mileage = mileage
        self.wheels = 4  # Атрибут по умолчанию для класса Car

    def description(self):
        description=(f"Модель: {self.model}, Год выпуска: {self.year}, Объём двигателя: {self.engine_capacity} л, "
                f"Цена: {self.price} рублей, Пробег: {self.mileage} км, Количество колёс: {self.wheels}")
        return description


car = Car("Toyota Corolla", 2020, 1.8, 1500000, 30000)
print("Информация о легковом автомобиле:")
print(car.description())

class Truck(Car):
    def __init__(self, model, year, engine_capacity, price, mileage):
        super().__init__(model, year, engine_capacity, price, mileage)
        self.wheels = 8  # У грузовика больше колёс

truck = Truck("Volvo FH", 2019, 12.8, 7000000, 150000)
print("\nИнформация о грузовике:")
print(truck.description())