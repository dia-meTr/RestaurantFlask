from dotenv import load_dotenv
import os

load_dotenv()


user = 'root' # os.environ.get("MYSQL_USER")
password = 'password' # os.environ.get("MYSQL_PASSWORD")
server = 'localhost' # os.environ.get("MYSQL_HOST")
database = 'restaurant' # os.environ.get("MYSQL_DB")
port = '3306' # os.environ.get("MYSQL_PORT")

#'mysql://localhost:3306/restaurant?user=root&password=password'

"""MYSQL_USER=root;
MYSQL_PASSWORD=password;
MYSQL_HOST=localhost;
MYSQL_DB=restaurant;
MYSQL_PORT=3306"""

class Config:
    DEBUG = True
    SECRET_KEY = os.urandom(32)
    SQLALCHEMY_DATABASE_URI = f'mysql://{user}:{password}' \
                              f'@{server}:{port}/{database}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
