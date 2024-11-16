class Animal:
    def __init__(self, name):
        self.__name = name

    def info(self):
        print("Name:", self.__name)


class Mammals(Animal):
    def move(self):
        print("I`m moving")


class Fish(Animal):
    def swim(self):
        print("I`m swimming")


class Cat(Mammals):
    def __init__(self, name, mouse):
        self.__mouse = mouse
        super().__init__(name)

    def info(self):
        super().info()
        print("Mouse:", self.__mouse)

    def catchMouse(self):
        print("I`m catching a mouse")
        self.__mouse += 1


class Dog(Mammals):
    def __init__(self, name, breed):
        self.__breed = breed
        super().__init__(name)

    def info(self):
        super().info()
        print("Breed:", self.__breed)


class GoldenFish(Fish):
    def __init__(self, name, wishes_granted):
        self.__wishes_granted = wishes_granted
        super().__init__(name)

    def info(self):
        super().info()
        print("Wishes granted:", self.__wishes_granted)

    def grantWish(self):
        print("I`m granting a wish!")
        self.__wishes_granted += 1


def choose_pet():
    print("Оберіть свого улюбленця:")
    print("1. Кіт")
    print("2. Собака")
    print("3. Золота рибка")

    choice = input("Введіть номер вибору (1, 2 або 3): ")
    name = input("Введіть ім'я вашого улюбленця: ")

    if choice == "1":
        cat = Cat(name, 0)
        print("Ви обрали кота!")
        cat.info()
        cat.move()
        cat.catchMouse()
        cat.info()
    elif choice == "2":
        breed = input("Введіть породу вашого собаки: ")
        dog = Dog(name, breed)
        print("Ви обрали собаку!")
        dog.info()
        dog.move()
    elif choice == "3":
        fish = GoldenFish(name, 0)
        print("Ви обрали золоту рибку!")
        fish.info()
        fish.grantWish()
        fish.info()
        fish.swim()
    else:
        print("Невірний вибір. Спробуйте ще раз.")


choose_pet()
