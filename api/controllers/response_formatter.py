from flask import jsonify


def reformat_tcmb_response(response_from_tcmb_as_dict):
    currencies_as_list = response_from_tcmb_as_dict["Tarih_Date"]["Currency"]

    reformatted_currencies_as_list = list()

    for currency_index in range(len(currencies_as_list)):
        reformatted_response = dict()

        reformatted_response["currency_code"] = currencies_as_list[currency_index]["@CurrencyCode"]
        reformatted_response["currency_name"] = currencies_as_list[currency_index]["CurrencyName"]
        reformatted_response["buying"] = currencies_as_list[currency_index]["ForexBuying"]
        reformatted_response["selling"] = currencies_as_list[currency_index]["ForexSelling"]

        reformatted_currencies_as_list.append(reformatted_response)

    return jsonify(reformatted_currencies_as_list)
