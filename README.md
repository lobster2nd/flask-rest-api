## Стек технологий  

<img src="https://img.shields.io/badge/Python - black?style=for-the-badge&logo=Python&logoColor=blue"/> <img src="https://img.shields.io/badge/Flask - black?style=for-the-badge&logo=Flask&logoColor=white"/>  

## Установка проекта локально (Linux)  
+ Склонировать репозиторий и перейти в него в командной строке:  
```
git clone https://github.com/lobster2nd/flask-rest-api.git
cd flask-rest-api
```  
+ Cоздать и активировать виртуальное окружение:   
```
python -m venv env
```  
```
source env/bin/activate
```  
+ Установить зависимости из файла requirements.txt:  
```
pip install -r requirements.txt
```  
+ Выполнить команду:  
```
python3 main.py
```

По умолчанию сервер запустится по адресу http://localhost:5000/.

## Работа с API

### Создание продукта


Чтобы создать новый продукт, отправьте POST-запрос на /api/v1/products с JSON-телом, содержащим информацию о продукте. Пример запроса с использованием cURL:

bash

```
curl -X POST http://localhost:5000/api/v1/product -H "Content-Type: application/json" -d '{"name": "Product Name", "price": 9.99}'
```

### Получение всех продуктов

Для получения списка всех продуктов отправьте GET-запрос на /api/v1/products. Пример запроса с использованием cURL:

bash
```
curl -X GET http://localhost:5000/api/v1/products
```

### Получение продукта по ID

Чтобы получить информацию о продукте по его уникальному идентификатору (ID), отправьте GET-запрос на /api/v1/product/<id>, где <id> - это идентификатор интересующего вас продукта. Пример запроса с использованием cURL:

bash
```
curl -X GET http://localhost:5000/api/v1/product/1
```

Замените 1 на реальный ID продукта, информацию о котором вы хотите получить.

## Помощь и поддержка

Если у вас возникли вопросы или проблемы, связанные с использованием API, пожалуйста, создайте issue в репозитории проекта.
