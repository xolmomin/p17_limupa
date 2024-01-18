from django.template import Library

register = Library()


@register.filter()
def sub(a, b):
    return a - int(b)
