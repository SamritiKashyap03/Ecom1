from django import template

register = template.Library()  # decorator


@register.filter(name='currency')
def currency(number):  # cart for reference
    return "₹"+str(number)


@register.filter(name='multiply')
def multiply(number , number1):  # cart for reference
    return number*number1
