from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('tinymce/', include('tinymce.urls')),
    path('contact/', views.contact, name='contact'),
    path('success/', views.successView, name='success'),
    path('', include('gallery.urls')),
    path('', include('blog.urls')),
    
    

    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

