from django import template
from blog.models import Category, Post
from django.db.models import Count
register = template.Library()

@register.inclusion_tag('blog/categories.html')

def show_categories(categories):
    categories = Category.objects.all().prefetch_related('category')
    categories = categories.annotate(post=Count('category'))
    post = Post.objects.all()
    return {'categories': categories, 'post':post}