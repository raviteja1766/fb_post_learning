from datetime import datetime
import pytz
from django.utils import timezone

def get_date_time_format(date_time):

    current_timezone = timezone.get_current_timezone() 
    date_obj = date_time.astimezone(current_timezone)
    created_time = datetime.strftime(date_obj, "%Y-%m-%d %H:%M:%S.%f%Z")
    return created_time