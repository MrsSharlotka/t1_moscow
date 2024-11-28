# Решение команды Five nights ay MISIS
___
## Описание
---
Наш сервис предназначен для анализа эффективности и «здоровья» спринтов на основе данных о состоянии задач.

## Функциональные возможности сервиса
---
Наше решение предоставляет возможность посмотреть метрики здоровья спринта, которые помогут оценить его качество и успешность.

### Переменные окружения
___
Файл `.env` должен лежать в корневой папке проекта со следующей структурой
```shell
# Database
DB_DRIVER=<ДРАЙВЕР_БАЗЫ_ДАННЫХ_ДЛЯ_БЕКЕНДА><"mongosh">
DB_HOST=<ХОСТ_БАЗЫ_ДАННЫХ>
DB_USERNAME=<НИКНЕЙМ_ПОЛЬЗОВАТЕЛЯ_БАЗЫ_ДАННЫХ>
DB_PASSWORD=<ПАРОЛЬ_ПОЛЬЗОВАТЕЛЯ_БАЗЫ_ДАННЫХ>
DB_NAME=<ИМЯ_БАЗЫ_ДАННЫХ>

# Backend
BACKEND_PORT=<ПОРТ_СЕРВЕРА>
BACKEND_HOST=<ХОСТ_СЕРВЕРА>
BACKEND_ALLOW_ORIGINS = ["http://localhost:3000", "https://localhost:3000"]
BACKEND_ALLOW_CREDENTIALS = True
BACKEND_ALLOW_METHODS = ["GET","POST","DELETE","PATCH","OPTIONS"]
BACKEND_ALLOW_HEADERS = ["Access-Control-Allow-Origin","Authorization","User-Agent","Connection","Host","Content-Type","Accept","Accept-Encoding"]

# Ml
ML_PORT:=<ПОРТ_СЕРВЕРА>
ML_HOST:=<ХОСТ_СЕРВЕРА>


# Auth
AUTH_SECRET_KEY=<СЕКРЕТНЫЙ_КЛЮЧ>
AUTH_ALGORITHM=<АЛГОРИТМ_ХЭШИРОВАНИЯ><"HS256">
AUTH_ACCESS_TOKEN_EXPIRE_MINUTES=30

# Frontend
DOMAIN=<ДОМЕННОЕ_ИМЯ><:80>
```
