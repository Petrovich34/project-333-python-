from tkinter.font import names

class Human:
    def __init__(self):
        self.__name = name
        self.age = 15

    def info(self):
        print("Name -", self.__name)

class Student(Human):
    def __init__(self, name, schoolName):
        self.__scName = schoolName
        super().__init__(name)

    def info(self):
        print("Student:")
        super().info()
        print("School: ", self.__scName)


h = Human("Vasya")
#print(h.__name)
h.info()


s = Student("Petya", "IT STEP")
s.info()