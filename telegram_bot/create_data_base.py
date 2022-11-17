import psycopg2
from psycopg2 import Error

try:
    # Подключение к существующей базе данных
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

    cursor.execute('DROP TABLE IF EXISTS slaves;')
    cursor.execute('DROP TABLE IF EXISTS cows;')

    # SQL-запрос для создания новой таблицы
    create_table_query = '''CREATE TABLE slaves
                                 (ID INT PRIMARY KEY     NOT NULL,
                                 WALLET         TEXT); '''
    # Выполнение команды: это создает новую таблицу
    cursor.execute(create_table_query)
    connection.commit()

    print("Таблица Работника успешно создана в PostgreSQL")

    # SQL-запрос для создания новой таблицы
    create_table_query = '''CREATE TABLE cows
                              (ID INT PRIMARY KEY     NOT NULL,
                              WALLET         TEXT,
                              COMPANY        TEXT); '''
    # Выполнение команды: это создает новую таблицу
    cursor.execute(create_table_query)
    connection.commit()

    print("Таблица Клиента успешно создана в PostgreSQL")

except (Exception, Error) as error:
    print("Ошибка при работе с PostgreSQL", error)
finally:
    if connection:
        cursor.close()
        connection.close()
        print("Соединение с PostgreSQL закрыто")