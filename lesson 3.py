import random

class Student:
    def __init__(self, name):
        self.name = name
        self.gladness = 15
        self.progress = 0
        self.energy = 20
        self.money = 20
        self.stress = 0
        self.alive = True

    def study(self):
        if self.money < 3:
            print("У Васі недостатньо грошей для навчання.")
            return
        print("Вася пішов навчатися")
        self.progress += 3; self.energy -= 3; self.gladness -= 2; self.money -= 3; self.stress += 2

    def sleep(self):
        print("Вася пішов спати")
        self.energy += 5; self.gladness += 1; self.stress -= 1

    def chill(self):
        if self.money < 5:
            print("У Васі недостатньо грошей для відпочинку.")
            return
        print("Вася пішов гуляти")
        self.energy -= 2; self.gladness += 6; self.progress -= 1; self.money -= 4; self.stress -= 5

    def work(self):
        print("Вася пішов на роботу")
        self.money += 15; self.energy -= 4; self.gladness -= 2; self.stress += 1

    def random_event(self):
        event = random.choice(["scholarship", "unexpected_expense", "stress_increase", "nothing"])
        if event == "scholarship":
            amount = random.randint(5, 15)
            self.money += amount
            print(f"Вася отримав стипендію на {amount} гривень!")
        elif event == "unexpected_expense":
            amount = random.randint(5, 10)
            self.money -= amount
            print(f"У Васі були непередбачені витрати на {amount} гривень.")
        elif event == "stress_increase":
            increase = random.randint(1, 3)
            self.stress += increase
            print(f"Вася відчуває додатковий стрес (+{increase})!")

    def info(self):
        print(f"На сьогодні {self.name}")
        print(f"Задоволення : {self.gladness}")
        print(f"Знання      : {self.progress}")
        print(f"Енергія     : {self.energy}")
        print(f"Гроші       : {self.money}")
        print(f"Стрес       : {self.stress}")

    def is_alive(self):
        if self.progress < 0:
            print("Вася отупів і він помер(")
            self.alive = False
        elif self.gladness < -10:
            print("У Васі глибока депресія (")
            self.alive = False
        elif self.progress > 80:
            print("Вася такий розумний, що достроково закінчив МКА ШАГ!")
            self.alive = False
        elif self.energy < 0:
            print("Вася зовсім знесилений")
            self.alive = False
        elif self.money < 0:
            print("Вася став бомжом")
            self.alive = False
        elif self.stress > 15:
            print("Вася перенапружився і не може далі навчатися!")
            self.alive = False

    def live(self, day):
        print(f"День №{day} з життя {self.name}")
        print("-" * 30)
        action = input("Вибери, що буде робити Вася: 1 - Навчатися, 2 - Гуляти, 3 - Спати, 4 - Працювати: ")
        if action == '1':
            self.study()
        elif action == '2':
            self.chill()
        elif action == '3':
            self.sleep()
        elif action == '4':
            self.work()
        else:
            print("Невірний вибір! Вася нічого не робить сьогодні.")

        self.random_event()
        self.info()
        self.is_alive()
        print()

st = Student("Вася")
for d in range(1, 366):
    if not st.alive:
        break
    st.live(d)
