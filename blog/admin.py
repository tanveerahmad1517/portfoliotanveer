from django.contrib import admin
from parler.admin import TranslatableAdmin
# Register your models here.
from .models import *


@admin.register(Category)
class CategoryAdmin(TranslatableAdmin):
    list_display = ['name', 'slug']

    def get_prepopulated_fields(self, request, obj=None):
            return {'slug': ('name',)}


@admin.register(Post)
class PostAdmin(TranslatableAdmin):
    list_display = ['title', 'slug',
                    'available', 'updated']
    list_filter = ['available', 'updated']
    list_editable = ['available']

    def get_prepopulated_fields(self, request, obj=None):
            return {'slug': ('title',)}

