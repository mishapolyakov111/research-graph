from pathlib import Path

import pytest
from pydantic import ValidationError

from research_graph.config import Settings, get_settings


def test_default_settings() -> None:
    settings = get_settings()
    assert settings.github_token is None
    assert settings.data_dir == Path("data")
    assert settings.log_level == "INFO"
    assert settings.request_timeout == 10.0
    assert settings.max_concurrency == 4


def test_settings_read_from_env(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("RG_LOG_LEVEL", "DEBUG")
    monkeypatch.setenv("RG_MAX_CONCURRENCY", "16")
    settings = Settings()
    assert settings.log_level == "DEBUG"
    assert settings.max_concurrency == 16


def test_rejects_invalid_concurrency(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("RG_MAX_CONCURRENCY", "0")
    with pytest.raises(ValidationError):
        Settings()


def test_rejects_invalid_timeout(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("RG_REQUEST_TIMEOUT", "-1")
    with pytest.raises(ValidationError):
        Settings()


def test_ensure_data_dir_creates_directory(tmp_path: Path) -> None:
    settings = Settings(data_dir=tmp_path / "new")
    path = settings.ensure_data_dir()
    assert path.is_dir()
