from datetime import datetime, date

def get_datetime(date_value):
    if isinstance(date_value, str):
        return datetime.strptime(date_value, '%Y.%m.%d')
    elif isinstance(date_value, date):
        return datetime(date_value.year, date_value.month, date_value.day)
    elif isinstance(date_value, datetime):
        return date_value
    else:
        raise ValueError('Invalid date value')

def get_day_difference(date1, date2):

    date1 = get_datetime(date1)
    date2 = get_datetime(date2)

    return (date2 - date1).days + 1