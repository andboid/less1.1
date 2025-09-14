## Запуск проекта через Docker Compose

В тестовом задании переменные окружения в `.env` не использовались.  
В продакшене они, конечно, будут подключены.

После поднятия контейнеров необходимо выполнить миграции и собрать статические файлы:
docker-compose exec web python manage.py migrate --noinput
docker-compose exec web python manage.py collectstatic

Вставлять эти команды в `Dockerfile` или `docker-compose.yml` , как я понял, не рекомендуется, так как это не соответствует best practices.  
Тем не менее, при необходимости их можно вынести в `entrypoint.sh` или указать в разделе `command` для сервиса `web` в `docker-compose.yml`.
