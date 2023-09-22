# YaCut

Yacat - это сервис укорачивания ссылок и API к нему. На большинстве сайтов адреса страниц довольно длинные и делиться такими ссылками не всегда удобно.
Yacat ассоциирует длинную пользовательскую ссылку с короткой, которую предлагает сам пользователь или предоставляет сервис.
Пользовательский интерфейс сервиса — страница с формой, состоящей из двух полей: обязательного для длинной исходной ссылки и необязательного для пользовательского варианта короткой ссылки.


# Возможности Yacut:

- генерация коротких ссылок и связь их с исходными длинными ссылками,
- переадресация на исходный адрес при обращении к коротким ссылкам.


# API проекта:

**Сервис обслуживает два эндпоинта:**

- /api/id/ — POST-запрос на создание новой короткой ссылки;
- /api/id/<short_id>/ — GET-запрос на получение оригинальной ссылки по указанному короткому идентификатору.

**Примеры запросов к API:**<br>

*GET получить оригинальной ссылки по указанному короткому идентификатору*<br>

`http://127.0.0.1:5000/api/id/<string:short_id>/`
<details><summary>Response 200 удачное выполнение запроса</summary>
{<br>
    "url": "string"<br>
}
</details>
<details><summary>Response 404 указанный короткий идентификатор не найден</summary>
{<br>
    "message": "Указанный id не найден"<br>
}
</details>

*POST создать новую короткую ссылку*<br>

`http://127.0.0.1:5000/api/id/`
<details><summary>Request</summary>
{<br>
    ""url": "string","<br>
    "custom_id": "string"<br>
}
</details>
<details><summary>Response 201 удачное выполнение запроса</summary>
{<br>
    "url": "string",,<br>
    "short_link": "string"<br>
}
</details>
<details><summary>Response 400 отсутствует тело запроса</summary>
{<br>
    "message": "Отсутствует тело запроса"<br>
}
</details>


# Технологии

![image](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue) Python 3.9<br>
![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white) Flask<br>
![SQLite](https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white) SQLite


# Инструкция по запуску

Клонировать репозиторий и перейти в него в командной строке:

```
git clone git@github.com:AtabekovaEkaterina/yacut.git
```

```
cd yacut
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv venv
```

* Если у вас Linux/macOS

    ```
    source venv/bin/activate
    ```

* Если у вас windows

    ```
    source venv/scripts/activate
    ```

Обновить менеджер пакетов pip и установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

В корневой директории проекта создайть файл .env, с указанием в нем значений:

```
FLASK_APP=yacut
FLASK_ENV=development
DATABASE_URI=sqlite:///db.sqlite3
SECRET_KEY=MY_SECRET_KEY
```

Запустить приложение:

```
flask run
```


# Автор

Екатерина Атабекова