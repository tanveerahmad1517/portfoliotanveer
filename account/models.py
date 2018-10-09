from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from cloudinary.models import CloudinaryField
from django.db.models import Q

GENDER_CHOICES = (
    ('Male', 'Male'),
    ('Female', 'Female'),
)

class AccountManager(models.Manager):
    def search(self, query=None):
        qs = self.get_queryset()
        if query is not None:
            or_lookup = (Q(user__icontains=query)
                        
                        )
            qs = qs.filter(or_lookup).distinct() # distinct() is often necessary with Q lookups
        return qs

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    location = models.CharField(max_length=50, null=True, blank=True)
    url = models.CharField(max_length=50, null=True, blank=True)
    job_title = models.CharField(max_length=50, null=True, blank=True)
    get_picture = CloudinaryField('Profile_pictures', default='user.png', null=True, blank=True)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, null=True, blank=True)
    
    objects = AccountManager()

    @property
    def image_url(self):
        if self.get_picture and hasattr(self.get_picture, 'url'):
            return self.get_picture.url
    def __str__(self):
        return self.user.username

    
    def get_screen_name(self):
        try:
            if self.user.get_full_name():
                return self.user.get_full_name()

            else:
                return self.user.username

        except Exception:  # pragma: no cover
            return self.user.username

# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)


# def save_user_profile(sender, instance, **kwargs):
#     instance.profile.save()



# post_save.connect(create_user_profile, sender=User)
# post_save.connect(save_user_profile, sender=User)