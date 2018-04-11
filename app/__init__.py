from flask import Flask # importing Flask from flask package installation
from config import Config # importing config class from config.py


app = Flask(__name__)
app.config.from_object(Config) # config items can be access with a dictionary syntax from app.config

from app import routes

