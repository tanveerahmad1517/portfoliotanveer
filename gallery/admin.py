from django.contrib import admin
from .models import Artwork, Gallery_Category
from parler.admin import TranslatableAdmin
@admin.register(Gallery_Category)
class Gallery_CategoryAdmin(TranslatableAdmin):
    list_display = ['name', 'slug']

    def get_prepopulated_fields(self, request, obj=None):
            return {'slug': ('name',)}



@admin.register(Artwork)
class PostAdmin(TranslatableAdmin):
    list_display = ['title',
                    'available']
    list_filter = ['available']
    list_editable = ['available']

