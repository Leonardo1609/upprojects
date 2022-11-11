import os

class DevelopmentConfig:
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = f"mysql://{os.getenv('USERNAME')}:{os.getenv('PASSWORD')}@{os.getenv('HOST')}/{os.getenv('DATABASE')}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    INERTIA_TEMPLATE = "base.html"

config = {
    'dev': DevelopmentConfig()
}
