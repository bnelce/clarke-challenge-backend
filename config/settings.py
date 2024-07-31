import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "postgresql://admin:admin@project_db:5432/suppliers")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
