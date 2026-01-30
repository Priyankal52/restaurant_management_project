import secrets
import string
from django.db import IntegrityError

def generate_coupon_code(length=10, model=None, feildname="code"):
   Generate a unique alphanumeric coupon code.

   Args:
    length (int) : Length of the coupon code (default=10)
    model (Django Model): Model class to check uniqueness against
    field_name (str): Field in model storing the coupon code 

Returns:
       str: Unique coupon code

if model is None:
    raise ValueError("Model must be provided to ensure uniqueness.")

    characters = string.ascii_uppercase + string.digits
    max_attempts = 100 

    if not model.objects.filter(**{field_name: code}).exists():
        return code 
    raise Execption("could not generate a unique coupon code after multiple attempts,")

from datatime import datetime
from django.utils import timezone
from .models import DailyOperatingHours

    def get_today_operating_hours():
        Returns today's operating hours as(open_time, close_time)
        if not hours set for today , returns (None, None)

        today_day = timezone.localtime(timezone.now()).strtime("%A")
       try:
        hours = DailyOperatingHours.get(day=today_day)
        return hours.open_time, hours.close_time
    except DailyOperatingHours.DoesNot:
        return None, None