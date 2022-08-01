import os
import requests

from .response_formatter import reformat_tcmb_response
from .xml_to_dict_converter import convert_xml_to_dict

url_for_tcmb = os.getenv("TCMB_URL")


def get_all_currencies_from_tcmb():
    all_currencies_from_tcmb_as_xml = requests.get(url_for_tcmb)

    all_currencies_from_tcmb_as_dict = convert_xml_to_dict(all_currencies_from_tcmb_as_xml.content)

    reformatted_currencies = reformat_tcmb_response(all_currencies_from_tcmb_as_dict)

    return reformatted_currencies
