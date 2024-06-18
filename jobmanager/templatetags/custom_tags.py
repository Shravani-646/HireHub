from django import template

register = template.Library()

@register.filter(name='concat_with_space')
def concat_with_space(value, arg):
    return f'{value} {arg}'
