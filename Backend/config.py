import os

class Config:
    # Secret key for sessions/security
    SECRET_KEY = os.getenv("SECRET_KEY", "dev_secret_key")

    # Database URL (Railway PostgreSQL or local SQLite fallback)
    SQLALCHEMY_DATABASE_URI = os.getenv(
        "DATABASE_URL",
        "sqlite:///test.db"
    )

    # Disable tracking (recommended)
    SQLALCHEMY_TRACK_MODIFICATIONS = False