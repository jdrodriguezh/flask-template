from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import config

db = SQLAlchemy()

# Create Application factory
def create_app(config_env=""):
  app = Flask(__name__)
  if not config_env:
    config_env = app.env
  # This could be changed dynamically with an env variable
  # "config.{}Config".format(config_env.capitalize())
  app.config.from_object(config.DevelopmentConfig)
  db.init_app(app)
  
  from app.cars.routes import cars_api
  from app.employees.routes import employees_api
  from app.main.routes import main_api

  app.register_blueprint(cars_api, url_prefix='/cars')
  app.register_blueprint(employees_api, url_prefix='/employees')
  app.register_blueprint(main_api)

  return app