import psycopg2

conn = psycopg2.connect(user="cvcode",

                        password="cvcode",
                        host="postgre_db",
                        port="5432",
                        database="cvcode_database")

cur = conn.cursor()

# Распечатать сведения о PostgreSQL
print("Информация о сервере PostgreSQL")
print(conn.get_dsn_parameters(), "\n")
# Выполнение SQL-запроса
cur.execute("SELECT version();")
# Получить результат
record = cur.fetchone()
print("Вы подключены к - ", record, "\n")

cur.execute('DROP TABLE IF EXISTS tasks;')
cur.execute('CREATE TABLE tasks (id serial PRIMARY KEY,'
            'wallet varchar (150) NOT NULL,'
            'task varchar (250) NOT NULL,'
            'date_added date DEFAULT CURRENT_TIMESTAMP);'
            )

cur.execute('INSERT INTO tasks (wallet, task)'
            'VALUES (%s, %s)',
            ('0xc86f36665B7BDc3FE727A4A57ab6190f0f98D2b6',
             'Если интеллектуально одаренный человек вкладывает себя в овладение любой абстрактной областью, например, математикой, то он рискует выпасть из социальных контактов. Неадаптивны те, кто вкладывает силы в абстрактную и отдаленную от жизни деятельность.')
            )

cur.execute('INSERT INTO tasks (wallet, task)'
            'VALUES (%s, %s)',
            ('0xc86f36665B7BDc3FE727A4A57ab6190f0f98D2b6',
             'Традиционно из общих соображений предполагалось, что среда в большей степени влияет на вербальный интеллект, чем на невербальный. Эмпирическая психогенетика показала противоположное: вербальный интеллект имеет большую наследуемость, чем невербальный.')
            )

conn.commit()

cur.close()
conn.close()
