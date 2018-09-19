from django.conf.urls import url
from django.urls import  path
from . import views

app_name = "account"

urlpatterns = [
    # path('edit/', views.edit, name='edit'),
    # url(r'^profile/$', views.view_profile, name='view_profile'),
    # url(r'^profile/(?P<pk>\d+)/$', views.view_profile, name='view_profile_with_pk'),
     url(r'^(?P<username>[^/]+)/$', views.profile, name='profile'),
    # path('edit/', views.UpdateViewProfile.as_view(), name='edit'),



]
# urlpatterns += [
#     path('accounts/', include('django.contrib.auth.urls')),
# ]
