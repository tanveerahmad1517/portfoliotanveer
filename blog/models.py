from django.db import models
from django.urls import reverse
from django.conf import settings
from django.contrib.auth.models import User
from parler.models import TranslatableModel, TranslatedFields


from django.db.models.signals import post_save
from django.utils.encoding import python_2_unicode_compatible
from django.utils.html import escape
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
import cloudinary
from cloudinary.models import CloudinaryField
class PostManager(models.Manager):
    def get_related(self, instance):
        post_one = self.get_queryset().filter(category=instance.category)
        qs = (post_one).exclude(id=instance.id).distinct()
        return qs



class Category(TranslatableModel):
    translations = TranslatedFields(
            name = models.CharField(max_length=200,
                                    db_index=True),
            slug = models.SlugField(max_length=200,
                                    db_index=True,
                                    unique=True)
        )

    class Meta:
        # ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
            return reverse('posts:product_list_by_category', args=[self.slug])
    # def get_absolute_url(self):
    #         return reverse('posts:profile', args=[self.pk])
                           

class Post(models.Model):
    title = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    description = models.TextField(blank=True)
    user =   models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL)
    category = models.ForeignKey(Category,
                                 related_name='category',
                                 null=True, blank=True,
                                 on_delete=models.SET_NULL)
    image = CloudinaryField("post_image/%Y/%m/%d",
                              blank=True)

    available = models.BooleanField(default=True)
    date = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    objects = PostManager()

    #class Meta:
    #    ordering = ('name',)
    #    index_together = (('id', 'slug'),)

    def get_absolute_url(self):
            return reverse('posts:detail',
                           args=[self.id, self.slug])

    class Meta:
        verbose_name = _('Post')
        verbose_name_plural = _('Posts')
        ordering = ('-date',)

    def __str__(self):
        return self.title

    
