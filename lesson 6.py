import random

class Human:
    def __init__(self, name, car=None, job=None):
        self.name = name
        self.house = House()
        self.car = car
        self.job = job
        self.money = 100

    def work(self):
        if self.job:
            self.money += self.job.salary
            print(f"{self.name} працює на посаді {self.job.name} і заробляє ${self.job.salary}")
        else:
            print(f"{self.name} безробітний і не може заробляти гроші.")

    def eat(self):
        if self.house.food > 0:
            self.house.food -= random.randint(1, 10)
            self.house.pollution += random.randint(1, 5)
            print(f"{self.name} поїв.")
        else:
            print(f"В будинку немає їжі. {self.name} йде за покупками.")

    def shopping(self):
        if self.money > 0:
            cost = random.randint(1, 10)
            food_amount = random.randint(1, 10)
            self.money -= cost
            self.house.food += food_amount
            print(f"{self.name} купує їжу: витрати ${cost}, отримано {food_amount} одиниць їжі.")
            if self.car:
                if self.car.drive(random.randint(1, 10) * 10):
                    print(f"{self.name} їде на {self.car.model} в магазин.")
                else:
                    print(f"{self.name} йде в магазин пішки, бо машина не на ходу.")
            else:
                print(f"{self.name} йде в магазин пішки.")
        else:
            print(f"У {self.name} недостатньо грошей для покупок.")

    def chill(self):
        if self.money > 10:
            self.money -= random.randint(10, 20)
            self.house.pollution += random.randint(1, 5)
            print(f"{self.name} гарно відпочив.")
        else:
            print(f"{self.name} не має достатньо грошей для відпочинку.")

    def cleaning(self):
        if self.house.pollution > 0:
            self.house.pollution -= random.randint(5, 15)
            print(f"{self.name} прибирає будинок.")
        else:
            print("Будинок чистий, прибирання не потрібне.")

    def info(self):
        print(f"Гроші - ${self.money}")
        print(self.house)
        if self.car:
            print(self.car)
        if self.job:
            print(self.job)

    def live(self, day):
        print(f"\nДень №{day}")
        print("Виберіть дію:")
        print("1 - Працювати")
        print("2 - Покупки")
        print("3 - Поїсти")
        print("4 - Відпочити")
        print("5 - Прибрати")
        print("6 - Пропустити день")

        try:
            choice = int(input("Ваш вибір: "))
        except ValueError:
            print("Невірний вибір! Пропускаємо день.")
            return

        if choice == 1:
            self.work()
        elif choice == 2:
            self.shopping()
        elif choice == 3:
            self.eat()
        elif choice == 4:
            self.chill()
        elif choice == 5:
            self.cleaning()
        elif choice == 6:
            print(f"{self.name} вирішив пропустити день.")
        else:
            print("Невірний вибір! Пропускаємо день.")

        if self.money > 1000 and self.car is None:
            print("Купляємо авто!")
            self.money -= 500
            self.car = Car("BMW X13")

        self.info()

    def is_alive(self):
        return self.money >= 0

class House:
    def __init__(self):
        self.food = 50
        self.pollution = 0

    def __str__(self):
        return f"Інформація про будинок: їжа - {self.food}, забруднення - {self.pollution}"

class Car:
    def __init__(self, model):
        self.model = model
        self.fuel = 60
        self.state = 100

    def drive(self, length):
        fuel_needed = length * 0.1
        if self.fuel < fuel_needed:
            print("Подорож не можлива, не вистачає пального.")
            return False
        else:
            self.fuel -= fuel_needed
            self.state -= length * 0.01
            print(f"Ми проїхали {length} км, витративши {fuel_needed} л пального.")
            return True

    def add_fuel(self, fuel):
        self.fuel = min(self.fuel + fuel, 60)
        print(f"Бак заправлений, тепер в ньому {self.fuel} літрів пального.")

    def __str__(self):
        return f"Авто {self.model}\nБензин - {self.fuel} л, стан - {int(self.state)} %"

class Job:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __str__(self):
        return f"Професія: {self.name}, зарплатня - ${self.salary}"

name = input("Введіть ім'я персонажа: ")
job = Job("Programmer", 300)
human = Human(name, job=job)

for day in range(1, 366):
    if not human.is_alive():
        print(f"{human.name} не зміг вижити.")
        break
    human.live(day)
