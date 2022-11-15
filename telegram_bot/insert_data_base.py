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

    data = [124, 123, 123]
    # Выполнение SQL-запроса для обновления таблицы
    insert_query = "INSERT INTO employee (id, name, wallet) values (%s, %s, %s)"
    cursor.execute(insert_query, data)
    connection.commit()
    count = cursor.rowcount
    print(count, "Запись успешно внесена")
    # Получить результат
    cursor.execute("SELECT * from employee")
    print("Результат", cursor.fetchall())


except (Exception, Error) as error:
    print("Ошибка при работе с PostgreSQL", error)
finally:
    if connection:
        cursor.close()
        connection.close()
        print("Соединение с PostgreSQL закрыто")