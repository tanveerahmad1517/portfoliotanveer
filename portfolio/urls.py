
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from .import views
from django.conf.urls.i18n import i18n_patterns
from django.utils.translation import gettext_lazy as _
urlpatterns = i18n_patterns(
	path('rosetta/', include('rosetta.urls')),
    path('admin/', admin.site.urls),
    path('tinymce/', include('tinymce.urls')),
    path('contact/', views.contact, name='contact'),
    path('success/', views.successView, name='success'),
    path('aboutMe/', views.about_me, name="aboutMe"),
    path('', include('gallery.urls')),
    path('blog/', include('blog.urls')),
    path('account/', include('account.urls')),

    
    # path('menus', include('menu.urls')),
 
)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
