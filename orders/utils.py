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