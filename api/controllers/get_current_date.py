import datetime


def current_date():
    date_time_object = datetime.datetime.now()

    current_date = date_time_object.strftime("%d.%m.%Y")

    return current_date
