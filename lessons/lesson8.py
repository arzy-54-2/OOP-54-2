import sqlite3

connect = sqlite3.connect("users.db")
cursor = connect.cursor()


cursor.execute('''
    CREATE TABLE IF NOT EXISTS users(
        user_id INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCHAR(30) NOT NULL,
        age INTEGER NOT NULL,
        hobby TEXT
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS grades(
        grade_id INTEGER PRIMARY KEY AUTOINCREMENT,
        subject VARCAHR(100) NOT NULL,
        grade INTEGER NOT NULL,
        userid INTEGER,
        FOREIGN KEY (userid) REFERENCES users(user_id)
    )
''')
connect.commit()


def add_user(name: str, age: int, hobby="None"):

    cursor.execute(
        'INSERT INTO users(name, age, hobby) VALUES (?,?,?)',
        (name, age, hobby)
    )
    connect.commit()
    print(f"{name} - Добавили")


# add_user("user", 14, "Спать")
# add_user("user2", 19, "Спать")
# add_user("user3", 22, "Спать")
# add_user("user4", 33, "Спать")


def add_grade(user_id, subject, grade):
    cursor.execute(
        'INSERT INTO grades(userid, subject, grade) VALUES (?,?,?)',
        (user_id, subject, grade)
    )
    connect.commit()

    print("Оценка за урок добавлена!!")

# add_grade(2, "Химия", 5)
# add_grade(1, "Физика", 3)
# add_grade(1, "ИЗО", 2)
# add_grade(1, "Физра", 4)
# add_grade(10, "Химия", 3)

def get_user_and_grades():
    cursor.execute('''
        SELECT users.name, grade.subjects, grades.grade
        FROM users FULL OUTER JOIN grades ON users.user_id = grades.userid
    ''')

    users = cursor.fetchall()

    for i in users:
        print(f"NAME: {i[0]}, SUBJECT: {i[1]}, GRADE: {i[2]}")

# get_user_and_grades()

# AVG() – Среднее значение
# MAX() – Максимальное значение
# MIN() – Минимальное значение  COUNT() SUM()

def get_average_age():
    cursor.execute('''
        SELECT SUM(age) FROM users
    ''')

    user = cursor.fetchone()

    print(user)

# get_average_age()


def create_view_highest_grade():
    cursor.execute('''
    CREATE VIEW IF NOT EXISTS highest_grade AS
    SELECT name, subject, grade
    FROM users JOIN grades ON users.user_id = grades.userid
    WHERE grade = (SELECT MAX(grade) FROM grades)
    ''')


    print("Представление создано или обновлено!!!")


create_view_highest_grade()


def highest_grade():
    cursor.execute('SELECT * FROM highest_grade')

    users = cursor.fetchall()

    print(users)

highest_grade()


