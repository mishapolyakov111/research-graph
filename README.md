# research-graph

![CI](https://github.com/mishapolyakov111/research-graph/actions/workflows/ci.yml/badge.svg)

Учебный проект курса по Python. В течение семестра здесь будет собираться пайплайн данных: загрузка данных из внешних источников (GitHub и другие), их хранение и обработка.

Сейчас в репозитории лежит каркас проекта: настройки через переменные окружения, логирование, CLI `rg` и инструменты контроля качества (ruff, mypy, pytest, pre-commit, GitHub Actions).

## Требования

- Python 3.12+
- [uv](https://docs.astral.sh/uv/)

## Установка

```bash
git clone https://github.com/mishapolyakov111/research-graph.git
cd research-graph
uv sync
```

## Конфигурация

Настройки читаются из переменных окружения с префиксом `RG_` или из файла `.env` в текущей директории.

| Переменная | Описание | По умолчанию |
|---|---|---|
| `RG_GITHUB_TOKEN` | Токен GitHub API | не задан |
| `RG_DATA_DIR` | Директория для данных | `data` |
| `RG_LOG_LEVEL` | Уровень логирования | `INFO` |
| `RG_REQUEST_TIMEOUT` | Таймаут запросов в секундах, от 0 до 300 | `10.0` |
| `RG_MAX_CONCURRENCY` | Число параллельных запросов, от 1 до 64 | `4` |

Пример `.env`:

```
RG_GITHUB_TOKEN=ghp_yourtoken
RG_LOG_LEVEL=DEBUG
```

## Использование

```bash
uv run rg --help
```

Показывает список команд: `version` и `check-config`.

```bash
uv run rg version
```

```
0.1.0
```

```bash
uv run rg check-config
```

```
2026-09-28 10:17:46,804 INFO research_graph.cli: Settings loaded
github_token: not set
data_dir: data
log_level: INFO
request_timeout: 10.0
max_concurrency: 4
```

Если токен задан, он выводится в маскированном виде, например `ghp_****1234`. Строка лога пишется в stderr, сводка в stdout.

## Разработка

```bash
uv run pytest
uv run ruff check .
uv run ruff format --check .
uv run mypy
```

Установка хуков pre-commit и их запуск на всех файлах:

```bash
uv run pre-commit install
uv run pre-commit run --all-files
```

## Структура проекта

```
research-graph/
├── .github/workflows/ci.yml   CI: линтер, форматирование, mypy, тесты
├── .pre-commit-config.yaml    хуки pre-commit
├── docs/lab1_report.md        отчёт по ЛР1
├── pyproject.toml             метаданные, зависимости, настройки инструментов
├── uv.lock                    зафиксированные версии зависимостей
├── src/research_graph/
│   ├── __init__.py            версия пакета
│   ├── cli.py                 CLI на Typer (команда rg)
│   ├── config.py              настройки на pydantic-settings
│   └── logging_setup.py       настройка логирования
└── tests/
    ├── conftest.py            изоляция тестов от окружения и .env
    ├── test_cli.py
    ├── test_config.py
    └── test_logging.py
```
