from dotenv import load_dotenv
from os import path

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, 'development.env'))

from flask import Flask
from api.views import get_currencies_from_tcmb


def create_app():
    app = Flask(__name__)

    app.register_blueprint(get_currencies_from_tcmb.bp)

    return app


app = create_app()
