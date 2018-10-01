from django.db import models
from django.urls import reverse
from django.template.defaultfilters import slugify

from django.utils import timezone

from django.db.models.signals import pre_delete
from django.dispatch import receiver
import cloudinary
# Create your models here.
from cloudinary.models import CloudinaryField
from parler.models import TranslatableModel, TranslatedFields


class ArtManager(models.Manager):
    def get_related(self, instance):
        art_one = self.get_queryset().filter(gcategory=instance.gcategory)
        qs = (art_one).exclude(id=instance.id).distinct()
        return qs

# class GalleryGroup(models.Model):

#     title = models.CharField(max_length=100, default='')
#     description = models.TextField()
#     slug = models.SlugField(unique=True)
#     galleryimage = CloudinaryField("galleryimage")

#     def __str__(self):
#         return self.title

#     def save(self, *args, **kwargs):
#                 self.slug = slugify(self.title)
#                 super(GalleryGroup, self).save(*args, **kwargs)

#     def get_absolute_url(self):
#         return reverse('gallery.views.gallery_detail', args=[str(self.id)])


class Gallery_Category(TranslatableModel):
    translations = TranslatedFields(
            name = models.CharField(max_length=200,
                                    db_index=True),
            slug = models.SlugField(max_length=200,
                                    db_index=True,
                                    unique=True)
        )
    description = models.TextField()
    galleryimage = CloudinaryField("galleryimage")

    class Meta:
        # ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
            return reverse('gallery:gallery_list_by_category',
                           args=[self.slug])


class Artwork(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    link = models.URLField(max_length=200)
    published_date = models.DateTimeField(default=timezone.now)
    art = CloudinaryField("art")
    gcategory = models.ForeignKey(Gallery_Category,
                                 related_name='gcategory',
                                 null=True, blank=True,
                                 on_delete=models.SET_NULL)
    available = models.BooleanField(default=True)
    objects = ArtManager()

    def publish(self):
        self.save()

    def __str__(self):
        return self.title

    # def get_absolute_url(self):
    #     return reverse('gallery.views.art_detail', args=[str(self.id)])









class Subscribe(models.Model):
  email_id = models.EmailField(null = True, blank = True)
  timestamp = models.DateTimeField(default=timezone.now)
  def __str__(self):
    return self.email_id