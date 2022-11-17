import psycopg2


connection = psycopg2.connect(user="cvcode",
                                  # пароль, который указали при установке PostgreSQL
                                  password="cvcode",
                                  host="postgre_db",
                                  port="5432",
                                  database="cvcode_database")


# Курсор для выполнения операций с базой данных
cursor = connection.cursor()
# Распечатать сведения о PostgreSQL
print("Информация о сервере PostgreSQL")
print(connection.get_dsn_parameters(), "\n")
# Выполнение SQL-запроса
cursor.execute("SELECT version();")
# Получить результат
record = cursor.fetchone()
print("Вы подключены к - ", record, "\n")

class DatBase:

    def __init__(self):
        # подключение к базе данных
        self.connection = psycopg2.connect(user="cvcode",
                                  # пароль, который указали при установке PostgreSQL
                                  password="cvcode",
                                  host="postgre_db",
                                  port="5432",
                                  database="cvcode_database")
        self.cursor = self.connection.cursor()

    # регистрация работника
    def add_viewer(self, data):
        with self.connection:
            self.data = data
            query = "INSERT INTO slaves (id, wallet) values (%s, %s)"
            self.cursor.executemany(query, [data])
            self.connection.commit()

    # проверка зарегистрирован ли работник в базе
    def check_viewer(self, user_id):
        self.user_id = user_id
        with self.connection:
            self.cursor.execute("SELECT *FROM slaves WHERE id = %s" % user_id)
            self.connection.commit()
            return bool(self.cursor.fetchall())

    # удаление работника из базы
    def remove_viewer(self, user_id):
        self.user_id = user_id
        with self.connection:
            self.cursor.execute("DELETE FROM slaves WHERE id = %s" % user_id)
            self.connection.commit()

    # регистрация клиента
    def add_jour(self, data):
        with self.connection:
            self.data = data
            query = "INSERT INTO cows (id, wallet, company) values (%s, %s, %s)"
            self.cursor.executemany(query, [data])
            self.connection.commit()

    # проверка зарегистрирован ли клиент в базе
    def check_jour(self, user_id):
        self.user_id = user_id
        with self.connection:
            self.cursor.execute("SELECT *FROM cows WHERE id = %s" % user_id)
            self.connection.commit()
            return bool(self.cursor.fetchall())

    # удаление клиента из базы
    def remove_jour(self, user_id):
        self.user_id = user_id
        with self.connection:
            self.cursor.execute("DELETE FROM cows WHERE id = %s" % user_id)
            self.connection.commit()
