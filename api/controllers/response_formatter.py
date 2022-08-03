from .get_current_date import current_date
from .get_current_time import current_time


def reformat_tcmb_response_for_all_currencies(response_from_tcmb_as_dict):
    currencies_as_list = response_from_tcmb_as_dict["Tarih_Date"]["Currency"]

    reformatted_currencies_as_list = list()

    for currency_index in range(len(currencies_as_list)):
        reformatted_response = dict()

        reformatted_response["currency_code"] = currencies_as_list[currency_index]["@CurrencyCode"]
        reformatted_response["currency_name"] = currencies_as_list[currency_index]["CurrencyName"]
        reformatted_response["buying"] = currencies_as_list[currency_index]["ForexBuying"]
        reformatted_response["selling"] = currencies_as_list[currency_index]["ForexSelling"]

        reformatted_currencies_as_list.append(reformatted_response)

    final_dict = dict()

    final_dict["date"] = current_date()
    final_dict["time"] = current_time()
    final_dict["currencies"] = reformatted_currencies_as_list

    return final_dict


def reformat_tcmb_response_for_specific_currency(all_currencies, requested_currency_code):
    requested_currency_as_dict = dict()

    for currency_index in range(len(all_currencies["currencies"])):
        if requested_currency_code.upper() == all_currencies["currencies"][currency_index]["currency_code"]:
            requested_currency_as_dict = all_currencies["currencies"][currency_index]

    final_dict = dict()

    final_dict["date"] = current_date()
    final_dict["time"] = current_time()
    final_dict[requested_currency_code] = requested_currency_as_dict

    if len(final_dict[requested_currency_code]) != 0:
        return final_dict

    return False
