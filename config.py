class Config:
  SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(Config):
  SQLALCHEMY_DATABASE_URI = "postgresql://postgres:josuedavid@localhost:5432/cars_api"
  DEBUG = True
  ENV = "development"


class ProductionConfig(Config):
  SQLALCHEMY_DATABASE_URI = "postgresql://owner:password@host:port/db_name"
  DEBUG = False
  ENV = "production"
