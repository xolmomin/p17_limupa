from django.template import Library

register = Library()


@register.filter()
def sub(a, b) -> int:
    return a - int(b)


@register.filter()
def add_url_query_params(a, b) -> str:
    result = f'?page={a}'
    if b.get('search'):
        result += f'&search={b["search"]}'
    return result
