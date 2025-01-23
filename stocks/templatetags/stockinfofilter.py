from django import template

register = template.Library()

@register.filter
def get(mapping, key):
    """Retrieve a key from a dictionary with default handling."""
    if isinstance(mapping, dict):
        return mapping.get(key, 'N/A')
    return "Invalid Data"

@register.filter
def removedot(value):
    """Remove dots from stock symbols to avoid HTML ID issues."""
    if isinstance(value, str):
        return value.replace('.', '_')
    return value
