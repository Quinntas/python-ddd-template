import datetime as dt

import pytz


def get_curr_dt(timezone: str = 'UTC'):
    return dt.datetime.now(pytz.timezone(timezone)).strftime("%d/%m/%Y-%H:%M:%S")


def convert_from_utc(_dt: str, timezone: str):
    return pytz.timezone('UTC').localize(dt.datetime.strptime(_dt, "%d/%m/%Y-%H:%M:%S")).astimezone(
        pytz.timezone(timezone)).strftime("%d/%m/%Y-%H:%M:%S")
