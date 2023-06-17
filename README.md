# Developer template

---

## Startup project
Эту команду необходимо ввести при инициализации проекта, она установит все зависимости для работы линтеров, автоформатеров и автосортировщиков импортов
### 1. Install all packages
```shel
poetry install --with dev
```

### 2. Init pre-commit
Эта команда настраивает Git хуки, они будут срабатывать при каждом коммите
```shell
poetry run pre-commit install
```

---

## Pre-commit
Хуки будут запускаться автоматически при каждом коммите

### Запуск проверки / форматирования кода без коммита
```shell
poetry run pre-commit run
```

## Управление зависимостями
### Добавление пакетов
Продакшен пакеты
```shell
poetry add [package name]
```

Девелоп пакеты
```shell
poetry add --group dev [packege name]
```

### Удаление пакетов
Продакшен пакеты
```shell
poetry remove [package name]
```

Девелоп пакеты
```shell
poetry remove --group dev [packege name]
```

## Экспорт зависимостей

Экспорт продакшен зависимостей
```shell
poetry export -f requirements.txt -o requirements.txt
```

Экспорт девелоп зависимостей
```shell
poetry export --with dev -f requirements.txt -o requirements.txt
```
