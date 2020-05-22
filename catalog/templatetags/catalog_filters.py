from django import template
import locale

register = template.Library()

@register.filter(name='currency')
def currency(value):
    try:
        locale.setlocale(locale.LC_ALL,'pt_BR.UTF-8')
        return locale.currency(value, grouping=True)
    except:
        locale.setlocale(locale.LC_ALL,'')
        loc = locale.localeconv()
        return locale.currency(value, loc['currency_symbol'], grouping=True)
