# checkers-backend

### Макет-[Figma](https://www.figma.com/file/zrSN1SvIU7xgRsSb9SlLd8/Checkers-with-MUI)
### Инструкция по установке и запуску сервера-backend

1. Проверить наличие установленного python-пакета pipenv
2. Склонировать репозиторий через Терминал командой: `git clone https://github.com/MarryP0ppins/checkers-backend.git`
3. Открыть склонированный проект
4. В командной строке проекта установить виртуальную среду и пакеты: `pipenv sync`

### Список доступных быстрых команд
`pipenv run <быстрая команда>`
1. update - `bash -c 'pipenv update && pipenv clean'` (обновляет файл Pipfile.lock, устанавливает новые и удаляет не используемые пакеты)
2. runserver - `python manage.py runserver` (запускает сервер-backend)
3. inspectdb - `python manage.py inspecdb`
4. makemigrations - `python manage.py makemigrations`
5. migrate - `python manage.py migrate`
6. autopep8 - `autopep8 app authentication project --recursive --in-place -a --exclude __pycache__/` (форматирует код)
