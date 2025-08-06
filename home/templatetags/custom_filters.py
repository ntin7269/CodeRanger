from django import template

register = template.Library()

@register.filter
def split_by_newline(value):
    """
    Splits a string by newline characters into a clean list.
    Removes empty lines and strips spaces.
    """
    if not value:
        return []
    return [line.strip() for line in value.splitlines() if line.strip()]

@register.filter
def split_by_comma(value):
    """
    Splits a string by commas into a clean list.
    Removes extra spaces around items.
    """
    if not value:
        return []
    return [item.strip() for item in value.split(",")]
