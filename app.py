from dotenv import load_dotenv
import os
from os import path

if os.getenv('FLASK_ENV') == "development":
    basedir = path.abspath(path.dirname(__file__))
    load_dotenv(path.join(basedir, 'development.env'))
else:
    basedir = path.abspath(path.dirname(__file__))
    load_dotenv(path.join(basedir, 'production.env'))

from flask import Flask
from api.views import get_currencies_from_tcmb


def create_app():
    app = Flask(__name__)

    app.register_blueprint(get_currencies_from_tcmb.bp)

    return app


app = create_app()
