.env не вводил для docker-compose, так как тестовое задание. В проде конечно они будут.
После поднятия docker compose, сделал миграцию: docker-compose exec web python manage.py migrate --noinput и команду для задания папки для всех статических файлов: docker-compose exec web python manage.py collectstatic.
