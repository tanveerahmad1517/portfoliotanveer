from django.contrib import admin
from .models import Artwork, Gallery_Category
from parler.admin import TranslatableAdmin
from parler.managers import TranslatableQuerySet, TranslatableManager
@admin.register(Gallery_Category)
class Gallery_CategoryAdmin(TranslatableAdmin):
    list_display = ['name', 'slug']

    def get_prepopulated_fields(self, request, obj=None):
            return {'slug': ('name',)}



admin.site.register(Artwork)

