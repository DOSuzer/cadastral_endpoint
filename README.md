# cadastral_endpoint
## Описание
Проект эмуляции внешнего сервера для [cadastral_number](https://github.com/DOSuzer/cadastral_number).
## Запуск проекта.
1. клонировать репозиторий
   ```
   git clone git@github.com:DOSuzer/cadastral_endpoint.git
   ```
2. Cоздать и активировать виртуальное окружение:
   ```
   cd adastral_endpoint
   py -3.10 -m venv env
   ```
   ```
   . venv/Scripts/activate - Windows
   . venv/bin/activate     - Linux
   ```
3. Установить зависимости из файла requirements.txt:
   ```
   python -m pip install --upgrade pip
   ```
   ```
   pip install -r requirements.txt
   ```
4. Запустить сервер:
   ```
   uvicorn main:app --reload --port 8001
   ```
## Работа:
При отправке GET запроса на 127.0.0.1:8001/data сервис возвращает True или False через случайный интервал времени (0..60 секунд).
