# Mining-Metrics-web-app

Mining Metrics - прототип веб-приложения автоматизированной системы управления технологическими процессами предприятия.

Для запуска c docker-compose предлагаю использовать данные команды:

    'docker-compose build'
    
    Для создания профиля администратора
    'docker-compose run --rm app sh -c "python manage.py createsuperuser"'

    'docker-compose up'

На сайте две основные страницы – главная и страница с отчетом.

Просмотр и редактирование отчета доступно только авторизованным пользователям.

Структура базы данных (модели Django): 

	- ConcentrateQuality - модель для хранения записей качественных показателей железорудного концентрата. В ней храним информацию о времени создания записи (автоматически); наименовании сырья; содержании компонентов (железо, кремний и т.д.); информацию о пользователе, создавшем запись; информацию о месяце отчета, к которому относится конкретная запись в виде внешнего ключа на другую модель ReportDate. Диапазон допустимых значений для показателей концентрата - от 0 до 100 (проценты).
    
	- ReportDate – модель с одним полем, хранящая информацию о дате отчета. Решил сделать отдельную модель для того, чтобы не было жесткой привязки по месяцам в зависимости от времени создания записи в модели ConcentrateQuality. По своему опыту знаю, что бывают ситуации, когда нужно что-то исправлять в отчетах предыдущего закрытого месяца по согласованию с администратором ресурса.

Два сериализатора ConcentrateQualitySerializer и ReportDateSerializer для конвертации объектов языка python (Django) в формат json (и обратно из json).

Для таблиц использовал Jspreadsheet. Поддерживается: копирование и вставка из Excel; сохранение в БД. Обмен данными между таблицей и БД происходит через интерфейс API.

Веб-приложение разворачивается в 3-х контейнерах docker: приложение, БД, веб-сервер.

Использовал: Django, DRF, PostgreSQL, Docker, uWSGI, Nginx.
Ниже примеры работы приложения:

![alt text](https://github.com/likeprogrsv/Mining-Metrics-web-app/blob/main/example-1.gif)
![alt text](https://github.com/likeprogrsv/Mining-Metrics-web-app/blob/main/example-2.gif)