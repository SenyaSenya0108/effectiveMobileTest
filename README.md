# _Тестовое задание для компании Effective Mobile_


### _Первичный деплой приложения_
```
    docker compose pull && docker compose build && docker compose up -d
```

### _Запуск приложения_
```
    docker compose up -d
```

### _Пересборка приложения_
```
    docker compose up -d --build
```

### _Остановить приложение_ 
```
    docker compose down
```

### _Использованные технологии_

* Docker Compose
* Python 3.12
* Nginx

### Архитектура 
```
effectiveMobileTest/
├── app.py                      # Python HTTP-сервер
├── docker-compose.yml          # Оркестрация контейнеров
├── docker-compose.yml          # Переменные окружения (шаблон)
├── README.md                   # Основная документация
├── STRUCTURE.md                # Этот файл — структура проекта
├── .gitignore                  # Игнорируемые файлы Git
├── .env.tmpl                   # Шаблон переменных окружения
├── backend/
│   └── Dockerfile              # Образ для backend (Python 3.12)
└── nginx/
    └── nginx.conf              # Конфигурация reverse proxy
```

## Описание файлов

| Файл | Описание |
|------|----------|
| `app.py` | Python HTTP-сервер на базе `http.server`. Отвечает на GET-запросы |
| `docker-compose.yml` | Конфигурация Docker Compose: сервисы nginx и backend |
| `backend/Dockerfile` | Docker-образ для backend на основе `python:3.12-slim` |
| `nginx/nginx.conf` | Конфигурация nginx как reverse proxy |
| `.env.tmpl` | Шаблон для файла переменных окружения `.env` |
| `.gitignore` | Список игнорируемых Git-файлов |

## Архитектура

```
┌─────────────┐      ┌─────────────┐      ┌─────────────┐
│   Client    │ ───► │    nginx    │ ───► │   backend   │
│  (порт 80)  │      │ (порт 80)   │      │  (порт 8081)│
└─────────────┘      └─────────────┘      └─────────────┘
```

## Сеть

Все контейнеры подключены к сети `app-network` (bridge driver).
