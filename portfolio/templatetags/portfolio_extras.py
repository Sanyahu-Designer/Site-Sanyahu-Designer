from django import template

register = template.Library()

@register.filter
def split_lines(value):
    """
    Retorna uma lista de linhas não vazias do texto
    """
    if not value:
        return []
    return [line.strip() for line in value.split('\n') if line.strip()]

@register.filter
def strip(value):
    """
    Remove espaços em branco do início e fim do texto
    """
    if not value:
        return ''
    return value.strip()
