from flask import Blueprint, abort

from api.controllers import get_all_currencies_from_tcmb, get_specific_currency_from_tcmb

bp = Blueprint('get_currencies_from_tcmb', __name__)


@bp.route("/all_currencies", methods=["GET"])
def get_all_currencies():
    response = get_all_currencies_from_tcmb()

    if response:
        return response
    abort(400)


@bp.route("/<currency_code>", methods=["GET"])
def get_specific_currency(currency_code):
    response = get_specific_currency_from_tcmb(currency_code)

    if response:
        return response
    abort(400)
