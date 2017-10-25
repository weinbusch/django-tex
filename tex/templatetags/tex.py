from django import template

register = template.Library()

@register.filter()
def euro(value):
    return '{:n} \\texteuro'.format(value)