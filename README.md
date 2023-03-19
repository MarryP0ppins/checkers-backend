# checkers-backend

### Инструкция по установке и запуску сервера-backend

1. Проверить наличие установленного python-пакета pipenv
2. Склонировать репозиторий через Терминал командой: `git clone https://github.com/MarryP0ppins/checkers-backend.git`
3. Открыть склонированный проект
4. В командной строке проекта установить виртуальную среду и пакеты: `pipenv sync`

### Список доступных быстрых команд
`pipenv run <быстрая команда>`
1. install - pipenv install (обновляет файл Pipfile.lock)
2. sync - pipenv sync (синхронизирует локальную виртуальную среду с файлом Pipfile.lock)
3. runserver - python manage.py runserver (запускает сервер-backend)
4. inspectdb - python manage.py inspecdb
5. makemigrations - python manage.py makemigrations
6. migrate - python manage.py migrate
