"""Test"""

class DataBase:
    "Comment"

    __instance = None

    def __new__(cls, *args, **kwargs):
        print("Создался образ БД")
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self, user, psw, port):
        print("Инициализировался образ БД")
        self.user = user
        self.psw = psw
        self.port = port

    def __del__(self):
        print("Удалился образ БД")
        DataBase.__instance = None

    def connect(self):
        "Comment"
        print(f"Соединение с образом БД: {self.user}, {self.psw}, {self.port}")

    def close(self):
        "Comment"
        print("Закрытие образа БД")

    def read(self):
        "Comment"
        return "Данные из образа БД"

    def write(self, data):
        "Comment"
        print(f"Запись в образ БД: {data}")

print("Изменения для гита")

database1 = DataBase('Files', 12345, 5432)
print(database1.__dict__)
database2 = DataBase('Docx', 54321, 3306)
print(database1.__dict__)
print(database2.__dict__)
delattr(database1,'port')
print(database1.__dict__)
print(database2.__dict__)
database1 = 0
print(database1)
print(database2)
