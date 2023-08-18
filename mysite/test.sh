python3 manage.py runserver

celery -A mysite worker -l debug -P eventlet
celery -A mysite beat -l debug

python3 manage.py makemigrations
python3 manage.py migrate



redis 失效后重新设计密码
redis-cli -p 6379 -a 12345678
Warning: Using a password with '-a' or '-u' option on the command line interface may not be safe.
Warning: AUTH failed
127.0.0.1:6379> config set requirepass 12345678
ok
127.0.0.1:6379> config get requirepass
1) "requirepass"
2) "12345678"
