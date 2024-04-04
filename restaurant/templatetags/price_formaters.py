from django import template

register = template.Library()


@register.filter
def currency_euro(value):
    return f"{value:.2f}\u20ac"
