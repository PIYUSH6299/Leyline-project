# config.py
import os

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "your_secret_key")

    # Database Configuration for PostgreSQL
    POSTGRES_USER = os.getenv("POSTGRES_USER", "leyline")
    POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD", "password")
    POSTGRES_HOST = os.getenv("POSTGRES_HOST", "db")
    POSTGRES_DB = os.getenv("POSTGRES_DB", "leyline")
    SQLALCHEMY_DATABASE_URI = (
        f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}/{POSTGRES_DB}"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
