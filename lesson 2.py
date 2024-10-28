class Student:
    print("Hi")
    count_of student = 0
    def __init__(self, name="No name", height=160, age=15):
        self.name = name
        self.height = height
        self.age = age

    def addYear(self):
        self.age +=1

    def study(self):
        print("я навчаюсь")

student1 = Student("Anton", 180)
print(student1.name)
print(student1.height)
student1.height = 185
print(student1.height)
print(student1.age)
student1.addYear()
student1.addYear()
student1.addYear()
print(student1.age)
student1.study()


student1 = Student()
print(student1.name)

student2 = Student()
print(student2.name)