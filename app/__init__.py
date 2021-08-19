from flask import Flask

#initialize the app
app = Flask(__name__, instance_relative_config=True)

#import the view
from app import views

#load the config file
app.config.from_object('config')
