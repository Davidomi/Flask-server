from dotenv import load_dotenv, dotenv_values
load_dotenv()

config = dotenv_values(".env")

class Config(object):
    TESTING = False
    SQLALCHEMY_DATABASE_URI = f'mysql://{config["DB_USER"]}:{config["DB_PASS"]}@{config["DB_HOST"]}/saga'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = "super secret key"

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = f'mysql://{config["DB_USER"]}:{config["DB_PASS"]}@{config["DB_HOST"]}/saga'
