.env не вводил для docker-compose, так как тестовое задание. В проде конечно они будут.
После поднятия docker compose, сделал миграцию: docker-compose exec web python manage.py migrate --noinput и команду для задания папки для всех статических файлов: docker-compose exec web python manage.py collectstatic.
Вставлять данные команды в Dockerfile/docker-compose как понял из документации не надо, так как это не соотвуствует best practice. Но это так же возможно через тот же самый entrypoint.sh в Dockerfile или в dcoker-compose в разделе с сервисом web в command.
