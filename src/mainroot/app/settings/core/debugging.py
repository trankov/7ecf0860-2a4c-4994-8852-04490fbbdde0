from app.settings.paths import BASE_DIR

DEBUG = (BASE_DIR / "DEBUG").exists()
DEBUG_PROPAGATE_EXCEPTIONS = False
