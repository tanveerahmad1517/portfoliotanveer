from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.utils.encoding import python_2_unicode_compatible
from django.utils.html import escape
from django.utils.translation import ugettext_lazy as _
from django.urls import reverse
from tinymce import HTMLField
from django.conf import  settings
from cloudinary.models import CloudinaryField
from mptt.models import MPTTModel, TreeForeignKey
from django.contrib.contenttypes.models import ContentType
from django.utils import timezone

class Category(MPTTModel):
  name = models.CharField(max_length=50, unique=True)
  parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children', db_index=True)
  slug = models.SlugField()

  class MPTTMeta:
    order_insertion_by = ['name']

  class Meta:
    unique_together = (('parent', 'slug',))
    verbose_name_plural = 'categories'

  def get_slug_list(self):
    try:
      ancestors = self.get_ancestors(include_self=True)
    except:
      ancestors = []
    else:
      ancestors = [ i.slug for i in ancestors]
    slugs = []
    for i in range(len(ancestors)):
      slugs.append('/'.join(ancestors[:i+1]))
    return slugs

  def __str__(self):
    return self.name






class Post(models.Model):
    user =   models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL)
    date = models.DateTimeField(auto_now_add=True)
    title = models.TextField(max_length=255)
    description = HTMLField('Description')
    category = TreeForeignKey('Category', on_delete=models.CASCADE, null=True,blank=True)
    default = models.ForeignKey('Category', on_delete=models.CASCADE, related_name='default_category', null=True, blank=True)
    image = CloudinaryField("Post_images")


    def get_absolute_url(self):
        return reverse('posts:all')



    class Meta:
        verbose_name = _('Post')
        verbose_name_plural = _('Posts')
        ordering = ('-date',)

    def __str__(self):
        return self.title
