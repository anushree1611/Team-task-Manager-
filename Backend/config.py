import os

class Config:
    # Secret key for session security
    SECRET_KEY = os.getenv("SECRET_KEY", "dev_secret_key")

    # Database configuration (Railway PostgreSQL OR fallback SQLite)
    SQLALCHEMY_DATABASE_URI = os.getenv(
        "DATABASE_URL",
        "sqlite:///test.db"
    ).replace("postgres://", "postgresql://", 1)

    # Disable tracking modifications (recommended)
    SQLALCHEMY_TRACK_MODIFICATIONS = False