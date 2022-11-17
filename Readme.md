# AI-SMM-Manager

Программа состоит из 3х модулей. 

1) База данных postgre: хранит информацию о зарегистрированных работниках
   и клиентах. Также хранит данные выполненных заданий.
   
2) Телеграм бот - регистрирует работников и клиентов, записывает номер 
    кошелька для осуществления расчетов.
   
3) Web App - сайт, на котором публикуются задания и номера кошельков работников. 
    Через сайт работники отправляют выполненное задание. На сайте также расположена 
   актуальная вакансия и ссылка на телеграм бота.
   
Устанавливается путем запуска docker compose.

!!!Внимание используется библиотека python, которая иногда выдает ошибку.
psycopg2==2.9.5

Рекомендации с официальной страницы библиотеки:
The Python header files. They are usually installed in a package such as python-dev or python3-dev. A message such as error: Python.h: No such file or directory is an indication that the Python headers are missing.

The libpq header files. They are usually installed in a package such as libpq-dev. If you get an error: libpq-fe.h: No such file or directory you are missing them.

The pg_config program: it is usually installed by the libpq-dev package but sometimes it is not in a PATH directory. Having it in the PATH greatly streamlines the installation, so try running pg_config --version: if it returns an error or an unexpected version number then locate the directory containing the pg_config shipped with the right libpq version (usually /usr/lib/postgresql/X.Y/bin/) and add it to the PATH:

$ export PATH=/usr/lib/postgresql/X.Y/bin/:$PATH
You only need pg_config to compile psycopg2, not for its regular usage.


---Запуск docker compose---

docker network create cv_code - перед запуском  
docker-compose up