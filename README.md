 ## Окружение
   
Для быстрого управления зависимостями стоит использовать виртуальное окружение от Pycharm (он автоматически предлагает его развернуть и сам распознает файл requirements.txt) или pipenv.
##Установить pip. 
В случае ubuntu:
<br>
```# apt install python3-pip```
<br>
**Внимание: на ubuntu обновлять pip следует только через пакетный менеджер apt. Может быть установлена только одна версия pip**

##Установить pipenv:

<br>```pip3 install --user pipenv```<br>
Объявить переменную `PIPENV_VENV_IN_PROJECT`. Данный пункт позволяет pipenv по умолчанию создавать virtual environment в папке с проектом. Для ubuntu это делается следующим образом:
<br> `echo "export PIPENV_VENV_IN_PROJECT=\"enabled\"" >> ~/.bashrc`<br>
<br> Используется pipenv в проекте следующим образом: нужно перейти в папку с проектом, убедиться, что присутствуют файл Pipfile и выполнить команду `pipenv install Pipfile`
<br> Устанавливать новые библиотеки командой `pipenv install lib-name`
<br />

##Установить geckodriver:

1. Выбрать соответствующую версию на [странице релизов](https://github.com/mozilla/geckodriver/releases) и скачать ее.
Пример: <br>```
wget https://github.com/mozilla/geckodriver/releases/download/v0.24.0
/geckodriver-v0.24.0-linux64.tar.gz ```<br>
2. Извлечь файл:
<br>```
tar -xvzf geckodriver* ```<br>
3. Сделать его исполняемым:
<br>```
chmod +x geckodriver ```<br>
4. Добавить в PATH, чтобы можно было его легко найти:
<br>```
export PATH=$PATH:/path-to-extracted-file/.```<br>

## Рекомендации
```
1. Pycharm Community
2. Все библиотеки подгружаются автоматически при выборе интепретатора 
из файлика requirements.txt
3. Окружение от Pycharm (предпочтительно), можно и pipenv, но Pycharm 
сам позволяет настроить отдельную среду без лишних манипуляций
4. Для корректной работы Firefox нужен geckodriver
```
## Конфиги
Используются конфиг: email.config. Примеры конфигов лежат в корне проекта.

## Запуск тестов:
```
pytest tests
```
Или точечно в Pycharm

