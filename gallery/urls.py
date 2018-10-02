from django.conf.urls import url
from . import views
from gallery.views import subscribe
from django.urls import path
app_name = 'gallery'
urlpatterns = [

    # url(r'^$', views.galleries, name='home'),
    path('subscribe/', views.subscribe, name = "subscribe"),
    path('', views.artwork_list, name="all"),

    path('<slug:gcategory_slug>/', views.artwork_list, 
         name='categorylist'),
    path('<slug:gcategory_slug>/', views.artwork_list, 
         name='gallery_list_by_category'),
    path('gallery/<int:pk>/', views.gallery_detail, 
         name='gallery_detail'),

    path('<art_id>', views.art_detail.as_view(), name="art"),
    path('<slug:category_slug>/', views.art_detail.as_view(), 
         name='categorylist'),
    # url(r'^gallery/(?P<gallery_title_slug>[\w\-]+)/', views.gallery_detail, name='gallery_detail'),
    # url(r'^art/(?P<art_id>[0-9]+)/$', views.art_detail, name='art'),
   
   


]

