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

class Post(models.Model):
    user =   models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL)
    date = models.DateTimeField(auto_now_add=True)
    title = models.TextField(max_length=255)
    description = HTMLField('Description')
    image = CloudinaryField("Post_images")


    def get_absolute_url(self):
        return reverse('posts:all')



    class Meta:
        verbose_name = _('Post')
        verbose_name_plural = _('Posts')
        ordering = ('-date',)

    def __str__(self):
        return self.title
from django.db import models

# Create your models here.
