import sqlite3

connection = sqlite3.connect("examen.db", timeout=5)  # Використовуємо іменований параметр
cur = connection.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS exam (login TEXT, password TEXT);")
connection.commit()

choice = int(input('Оберіть дію:\n1 - Зареєструватися\n2 - Увійти\nВаш вибір: '))

if choice == 1:
    print("\nРеєстрація нового користувача:")
    login = input('Введіть бажаний логін: ')

    cur.execute("SELECT * FROM exam WHERE login = ?", (login,))
    existing_user = cur.fetchone()

    if existing_user:
        print('⚠️ Цей логін вже зайнятий. Спробуйте інший.')
    else:
        password = input('Введіть пароль: ')
        cur.execute("INSERT INTO exam (login, password) VALUES (?, ?)", (login, password))
        connection.commit()
        print(f'✅ Реєстрація успішна! Ласкаво просимо, {login}!')

elif choice == 2:
    print("\nВхід до системи:")
    login = input('Введіть логін: ')
    password = input('Введіть пароль: ')

    cur.execute("SELECT * FROM exam WHERE login = ? AND password = ?", (login, password))
    user = cur.fetchone()

    if user:
        print(f'✅ Вхід успішний! Вітаємо, {login}!')
    else:
        print('❌ Невірний логін або пароль. Спробуйте ще раз.')

connection.close()
