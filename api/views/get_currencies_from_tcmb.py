from flask import Blueprint, request

from api.controllers import get_all_currencies_from_tcmb


bp = Blueprint('get_currencies_from_tcmb', __name__)


@bp.route("/all_currencies", methods=["GET"])
def get_all_currencies():
    response = get_all_currencies_from_tcmb()
    return response
