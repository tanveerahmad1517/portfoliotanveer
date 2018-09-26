from django import template
from gallery.models import Gallery_Category
register = template.Library()

@register.inclusion_tag('menu.html')
def show_menu(menu):
    gcategories = Gallery_Category.objects.all()
    return {'gcategories': gcategories}