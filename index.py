from flask import Flask
from app import create_app
from config import config

config_app = config['dev']

app: Flask = create_app(config_app)
app.run()
