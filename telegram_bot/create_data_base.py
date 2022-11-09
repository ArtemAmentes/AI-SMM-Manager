import psycopg2
from psycopg2 import Error

try:
    # Подключение к существующей базе данных
    connection = psycopg2.connect(user="cvcode",
                                  # пароль, который указали при установке PostgreSQL
                                  password="cvcode",
                                  host="45.8.248.84",
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

    # SQL-запрос для создания новой таблицы
    create_table_query = '''CREATE TABLE users
                              (ID INT PRIMARY KEY     NOT NULL,
                              NAME           TEXT    NOT NULL,
                              WALLET         TEXT); '''
    # Выполнение команды: это создает новую таблицу
    cursor.execute(create_table_query)
    connection.commit()
    print("Таблица успешно создана в PostgreSQL")