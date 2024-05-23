from django import template

register = template.Library()

@register.filter()
def range(min=5):
    return range(min)

@register.filter
def remove_trailing_zero(value):
    """
    Removes trailing zeros after the decimal point if present.
    """
    if isinstance(value, float):
        if ".0" in str(value) and str(value)[-1] == "0":
            str_val = "{:.0f}".format(value)
            return str_val if str_val[-1]!= '.' else str_val[:-1]
        else:
            return value
    else:
        return value