import datetime, pytz

import jinja2
from django_jinja import library


@library.filter
def post_date_format(value):
    local_tz = pytz.timezone('America/Toronto')
    dt = datetime.datetime.strptime(value, '%Y-%m-%d %H:%M:%S').replace(tzinfo=pytz.utc).astimezone(local_tz)
    return dt.strftime('On %B %d at %I:%M %p')


@library.filter
def url_target_blank(text):
    return text.replace('<a ', '<a target="_blank" ')


@library.filter
def to_date(value):
    return datetime.datetime.strptime(value, '%Y-%m-%d %H:%M:%S')


@library.filter
def time_format(value):
    local_tz = pytz.timezone('America/Toronto')
    dt = datetime.datetime.strptime(value, '%Y-%m-%d %H:%M:%S').replace(tzinfo=pytz.utc).astimezone(local_tz)
    return dt.strftime('%I:%M %p')
