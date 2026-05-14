from django import template
register = template.Library()



@register.filter(name="f3upper")
def first_three_upper(value):
    result = value[:3].upper() + value[3:]
    return result


