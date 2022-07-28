from datetime import datetime
from django import template

register = template.Library()


def change_format(value: datetime):
    return value.strftime("%B %d, %I:%M %p")


register.filter("change_format", change_format)
