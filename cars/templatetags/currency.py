# car/templatetags/currency.py
from django import template

register = template.Library()

@register.filter
def rupiah(value):
    try:
        value = float(value)
        return "Rp{:,.0f}".format(value).replace(",", "X").replace(".", ",").replace("X", ".")
    except:
        return value

@register.filter
def percent(value):
    try:
        value = float(value)
        return "{:,.0f}%".format(value).replace(",", "X").replace(".", ",").replace("X", ".")
    except:
        return value
