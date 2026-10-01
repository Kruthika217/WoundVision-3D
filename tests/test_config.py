from pathlib import Path

from woundvision.core.config import (
    PROJECT_NAME,
    PROJECT_VERSION,
    PROJECT_ROOT,
    DATA_DIR,
    MODELS_DIR,
    RESEARCH_DIR,
    ensure_directories,
)


def test_project_name():
    assert PROJECT_NAME == "WoundVision 3D"


def test_project_version():
    assert PROJECT_VERSION == "0.1.0"


def test_project_root_exists():
    assert PROJECT_ROOT.exists()
    assert PROJECT_ROOT.is_dir()


def test_core_directories():
    ensure_directories()

    assert DATA_DIR.exists()
    assert MODELS_DIR.exists()
    assert RESEARCH_DIR.exists()


def test_project_root_is_path():
    assert isinstance(PROJECT_ROOT, Path)