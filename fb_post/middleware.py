import time
from django.db import connection

def TimeMiddleware(get_response):

    def wrapper(request):
        starttime = time.time()
        response = get_response(request)
        endtime = time.time()
        print("Execution Time:", endtime-starttime)
        return response

    return wrapper

def DBhitsMiddleware(get_response):

    def wrapper(request):
        print(len(connection.queries))
        response = get_response(request)
        print(len(connection.queries))
        return response

    return wrapper

import pytz

from django.utils import timezone

class TimezoneMiddleware(object):

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        tz_info = request.headers.get('timezone')
        if tz_info:
            timezone.activate(pytz.timezone(tz_info))
        response = self.get_response(request)
        return response
