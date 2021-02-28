from flask import Flask
from .config import Config

#UPLOAD_FOLDER = './app/static/uploads'
UPLOAD_FOLDER = 'uploads/'

app = Flask(__name__)
app.config.from_object(Config)

from app import views
