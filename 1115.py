def calculator():
    a = float(input("Введіть перше число: "))
    b = float(input("Введіть друге число: "))
    operation = input("Введіть дію (+, -, *, /): ")
    if operation == '+':
        print("Результат:", a + b)
    elif operation == '-':
        print("Результат:", a - b)
    elif operation == '*':
        print("Результат:", a * b)
    elif operation == '/' and b != 0:
        print("Результат:", a / b)
    else:
        print("Помилка")

calculator()
