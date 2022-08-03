import datetime


def current_time():
    date_time_object = datetime.datetime.now()

    current_time = date_time_object.strftime("%H:%M:%S")

    return current_time
