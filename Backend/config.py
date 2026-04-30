import os

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "dev_secret_key")

    db_url = os.getenv("DATABASE_URL", "sqlite:///test.db")
    # Railway gives postgres:// — SQLAlchemy needs postgresql://
    if db_url.startswith("postgres://"):
        db_url = db_url.replace("postgres://", "postgresql://", 1)

    SQLALCHEMY_DATABASE_URI = db_url
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ENGINE_OPTIONS = {
        "pool_pre_ping": True,  # avoids hanging connections
    }