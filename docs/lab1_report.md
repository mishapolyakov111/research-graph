# Отчёт по ЛР1

## Уровень

Выполнен базовый уровень.

## Что сделано

- Проект создан через `uv init --lib`, код лежит в `src/research_graph`, версия Python и зависимости зафиксированы в `.python-version` и `uv.lock`.
- `config.py`: класс `Settings` на `pydantic-settings` с префиксом `RG_`, валидацией границ для `request_timeout` и `max_concurrency` и методом `ensure_data_dir`.
- `logging_setup.py`: логирование в stderr, очистка старых обработчиков, приглушение сторонних библиотек.
- `cli.py`: команды `version` и `check-config`, токен выводится только в маскированном виде.
- Тесты на значения по умолчанию, переменные окружения, валидацию, логирование и CLI. Покрытие 100 %.
- Настроены ruff, mypy, pre-commit и GitHub Actions.
