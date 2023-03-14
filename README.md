# Mining-Metrics-web-app

Прототип веб-приложения автоматизированной системы управления технологическими процессами предприятия.

Для запуска c docker-compose предлагаю использовать данные команды:
    'docker-compose build'
    
    <!-- Для создания профиля администратора -->
    'docker-compose run --rm app sh -c "python manage.py createsuperuser"'

    'docker-compose up'

Использовал: Django, DRF, PostgreSQL, Docker.
Ниже примеры работы приложения:

![alt text](https://github.com/likeprogrsv/Mining-Metrics-web-app/blob/main/example-1.gif)
![alt text](https://github.com/likeprogrsv/Mining-Metrics-web-app/blob/main/example-2.gif)