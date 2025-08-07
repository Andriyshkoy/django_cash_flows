import os

import dj_database_url
from dotenv import load_dotenv

from .base import *  # noqa: F401,F403
from .base import BASE_DIR

load_dotenv(BASE_DIR / ".env.prod")

SECRET_KEY = os.getenv("SECRET_KEY")
DEBUG = os.getenv("DEBUG", "false").lower() == "true"
ALLOWED_HOSTS = os.getenv("ALLOWED_HOSTS", "").split(",")

DATABASES = {"default": dj_database_url.config(env="DATABASE_URL", conn_max_age=600)}

STATIC_ROOT = BASE_DIR / "static"

CSRF_TRUSTED_ORIGINS = os.getenv("CSRF_TRUSTED_ORIGINS", "").split(",")
