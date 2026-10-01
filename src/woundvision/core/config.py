from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[3]

DATA_DIR = PROJECT_ROOT / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
PROCESSED_DATA_DIR = DATA_DIR / "processed"
EXTERNAL_DATA_DIR = DATA_DIR / "external"
SYNTHETIC_DATA_DIR = DATA_DIR / "synthetic"

MODELS_DIR = PROJECT_ROOT / "models"

EXPERIMENTS_DIR = PROJECT_ROOT / "experiments"
BASELINES_DIR = EXPERIMENTS_DIR / "baselines"
ABLATION_DIR = EXPERIMENTS_DIR / "ablation"
RESULTS_DIR = EXPERIMENTS_DIR / "results"

RESEARCH_DIR = PROJECT_ROOT / "research"
LITERATURE_DIR = RESEARCH_DIR / "literature"
HYPOTHESES_DIR = RESEARCH_DIR / "hypotheses"
PROTOCOLS_DIR = RESEARCH_DIR / "protocols"
NOTES_DIR = RESEARCH_DIR / "notes"

APP_DIR = PROJECT_ROOT / "app"
TESTS_DIR = PROJECT_ROOT / "tests"

PROJECT_NAME = "WoundVision 3D"
PROJECT_VERSION = "0.1.0"

SUPPORTED_IMAGE_EXTENSIONS = {
    ".jpg",
    ".jpeg",
    ".png",
    ".bmp",
    ".tif",
    ".tiff",
}

SUPPORTED_VIDEO_EXTENSIONS = {
    ".mp4",
    ".mov",
    ".avi",
    ".mkv",
}


def ensure_directories() -> None:
    directories = [
        DATA_DIR,
        RAW_DATA_DIR,
        PROCESSED_DATA_DIR,
        EXTERNAL_DATA_DIR,
        SYNTHETIC_DATA_DIR,
        MODELS_DIR,
        EXPERIMENTS_DIR,
        BASELINES_DIR,
        ABLATION_DIR,
        RESULTS_DIR,
        RESEARCH_DIR,
        LITERATURE_DIR,
        HYPOTHESES_DIR,
        PROTOCOLS_DIR,
        NOTES_DIR,
        APP_DIR,
        TESTS_DIR,
    ]

    for directory in directories:
        directory.mkdir(parents=True, exist_ok=True)