from dtlcatalog.models import Category
from django import template

register = template.Library()

@register.inclusion_tag("categories.html")
def category_list(request_path):
    active_categories = Category.objects.filter(is_active=True)
    return {
        'active_categories': active_categories,
        'request_path': request_path
    }
