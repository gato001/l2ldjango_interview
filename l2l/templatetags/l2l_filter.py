from django import template
from datetime import datetime

register = template.Library()

@register.filter
def format_date(value):
    # Check if the value is already a datetime object
    if isinstance(value, datetime):
        return value.strftime("%Y-%m-%d %H:%M:%S")
    
    #Convert string to datetime object
    try:
        value =  datetime.strptime(value, "%Y-%m-%dT%H:%M:%S")
    except ValueError:
        return value
    
    #format datetime object as string
    return value.strftime("%Y-%m-%d %H:%M:%S")