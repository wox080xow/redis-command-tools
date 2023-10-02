from pathlib import Path
import environ

env = environ.Env(
    DEBUG=(bool, False),
    # LOG
    LOG_LEVEL=(str, "INFO"),
)
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent
# Read env file
environ.Env.read_env(BASE_DIR.parent / ".env")
LOG_LEVEL = env("LOG_LEVEL").upper()
DEBUG = env("DEBUG")

HELLO = env("HELLO")

LOCAL_APPS = [
    "say_hello",
]

INSTALLED_APPS = LOCAL_APPS
