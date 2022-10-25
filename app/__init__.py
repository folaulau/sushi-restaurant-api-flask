from flask import Flask
import sys
import logging.config
# from flask_sqlalchemy import SQLAlchemy

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s %(lineno)d %(name)-12s %(levelname)-8s %(message)s",
    handlers=[
        logging.StreamHandler(sys.stdout)
    ]
)

app = Flask(__name__)

# Postgres Database
# host = '127.0.0.1'
# port = 5432
# username = 'postgres'
# password = 'postgres'
# database = 'sushi_api_db'
#
# app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql://{username}:{password}@{host}:{port}/{database}"
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# db = SQLAlchemy(app)

from app.controller import info_controller
from app.controller import user_controller

if __name__ == '__main__':
    app.run(debug=True)

