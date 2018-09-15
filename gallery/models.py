from django.db import models
from django.urls import reverse
from django.template.defaultfilters import slugify

from django.utils import timezone

from django.db.models.signals import pre_delete
from django.dispatch import receiver
import cloudinary
# Create your models here.
from cloudinary.models import CloudinaryField

class GalleryGroup(models.Model):

    title = models.CharField(max_length=100, default='')
    description = models.TextField()
    slug = models.SlugField(unique=True)
    galleryimage = CloudinaryField("galleryimage")

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
                self.slug = slugify(self.title)
                super(GalleryGroup, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('gallery.views.gallery_detail', args=[str(self.id)])


class Artwork(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    link = models.URLField(max_length=200)
    published_date = models.DateTimeField(default=timezone.now)
    art = CloudinaryField("art")
    group = models.ForeignKey('GalleryGroup', on_delete=models.CASCADE)

    def publish(self):
        self.save()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('gallery.views.art_detail', args=[str(self.id)])
