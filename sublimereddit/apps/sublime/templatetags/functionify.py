from django import template
register = template.Library()


def functionify(title):
    """
    Build function name PEP8 style.
    """
    return title[0:20].strip().replace(' ', '_').replace('.', '')

register.filter(functionify)
