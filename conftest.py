from __future__ import annotations
from pathlib import Path
import shutil
import os
import pytest


def pytest_addoption(parser: pytest.Parser) -> None:
    """
    Флаги:
    --no-clean-allure       — отключить авто-очистку allure-results.
    --clean-allure-verbose  — показать путь и статус очистки.
    """
    parser.addoption("--no-clean-allure", action="store_true", default=False)
    parser.addoption("--clean-allure-verbose", action="store_true", default=False)

def _resolve_allure_dir(config: pytest.Config) -> Path:
    """
    Определяет директорию allure-results:
    1) --alluredir (если задан)
    2) ALLURE_RESULTS_DIR из окружения
    3) 'allure-results' в корне проекта
    Возвращает абсолютный Path.
    """
    alluredir = None
    try:
        alluredir = config.getoption("--alluredir", default=None)
    except Exception:
        alluredir = None

    if not alluredir:
        alluredir = os.environ.get("ALLURE_RESULTS_DIR", "allure-results")

    base = Path(config.rootpath)
    path = Path(alluredir)
    return (base / path).resolve() if not path.is_absolute() else path.resolve()

def _safe_clean_dir(dir_path: Path, project_root: Path) -> str:
    """
    Безопасно удаляет папку результатов и создаёт пустую.
    Возвращает краткий статус для логов.
    """
    dir_path = dir_path.resolve()
    project_root = project_root.resolve()

    # Безопасность: не удаляем корень проекта и не выходим за его пределы
    if dir_path == project_root:
        return f"SKIP: {dir_path} == project root"
    if project_root not in dir_path.parents:
        return f"SKIP: {dir_path} is outside project {project_root}"

    existed = dir_path.exists()
    if existed:
        shutil.rmtree(dir_path, ignore_errors=True)
    dir_path.mkdir(parents=True, exist_ok=True)
    return f"{'REMOVED' if existed else 'CREATED'}: {dir_path}"

@pytest.hookimpl(tryfirst=True)
def pytest_sessionstart(session: pytest.Session) -> None:
    """
    Запускается один раз перед прогоном.
    Чистит папку allure-results на главном процессе.
    """
    config = session.config

    # xdist: пропускаем воркеры
    if getattr(config, "workerinput", None) is not None:
        return

    if config.getoption("--no-clean-allure"):
        if config.getoption("--clean-allure-verbose"):
            tr = config.pluginmanager.getplugin("terminalreporter")
            if tr:
                tr.write_line("[allure-clean] SKIP: disabled by --no-clean-allure")
        return

    project_root = Path(config.rootpath)
    results_dir = _resolve_allure_dir(config)
    status = _safe_clean_dir(results_dir, project_root)

    # Отладочный вывод по флагу
    if config.getoption("--clean-allure-verbose"):
        tr = config.pluginmanager.getplugin("terminalreporter")
        if tr:
            tr.write_line(f"[allure-clean] root={project_root}")
        if tr:
            tr.write_line(f"[allure-clean] {status}")


pytest_plugins = (
    "fixtures.pages",
    "fixtures.browsers"
)
