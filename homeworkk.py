users = {
    "Олександр": "Молодь",
    "Анна": "Дорослі",
    "Марія": "Літні люди",
    "Іван": "Молодь"
}

def checker(var):
    if not isinstance(var, str):
        raise TypeError(f"var {type(var)} is not string")
    return var

print("Запуск програми")
print("Доступні користувачі:", ", ".join(users.keys()))

try:
    name = input("Введіть ім'я користувача: ")
    checker(name)

    if name in users:
        print(f"Вікова група користувача {name}: {users[name]}")
    else:
        print(f"Користувача з ім'ям {name} не знайдено у словнику.")
except TypeError as ex:
    print(ex)
finally:
    print("Програма завершила роботу")
