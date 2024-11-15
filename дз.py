class Vehicle:
    def __init__(self, brand):
        self.__brand = brand

    def info(self):
        print("Бренд:", self.__brand)


class LandVehicle(Vehicle):
    def drive(self):
        print("Їду по землі")


class WaterVehicle(Vehicle):
    def sail(self):
        print("Пливу по воді")


class Car(LandVehicle):
    def __init__(self, brand):
        super().__init__(brand)

    def info(self):
        super().info()


class Boat(WaterVehicle):
    def __init__(self, brand):
        super().__init__(brand)

    def info(self):
        super().info()


def choose_vehicle():
    print("Оберіть транспорт:")
    print("1. Автомобіль (Tesla)")
    print("2. Автомобіль (BMW)")
    print("3. Човен (Yamaha)")

    choice = input("Введіть номер вибору (1, 2 або 3): ")

    if choice == "1":
        car = Car("Tesla")
        car.info()
        car.drive()
    elif choice == "2":
        car = Car("BMW")
        car.info()
        car.drive()
    elif choice == "3":
        boat = Boat("Yamaha")
        boat.info()
        boat.sail()
    else:
        print("Невірний вибір. Спробуйте ще раз.")


choose_vehicle()
