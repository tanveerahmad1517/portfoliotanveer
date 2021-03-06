
from django.conf.urls import url
from .import views
# from posts.views import HomeView
from django.urls import path
# from account.views import profile
app_name = 'posts'

urlpatterns = [
    # url(r'^user/(\w+)/$', views.profile, name='profile'),
    path('user/<username>/', views.profile, 
         name='profile'),
    path('list', views.post_list.as_view(), name="all"),
    # path('<slug:category_slug>/', views.post_list.as_view(), 
    #      name='categorylist'),

    path('<slug:category_slug>/', views.post_list.as_view(), 
         name='product_list_by_category'),

    path('<int:id>/<slug:slug>/', views.detail.as_view(),
         name='detail'),  
     path('search', views.search, name='search'),

    
    # path('posts/', views.posts, name='all'),
    # path('post/<int:pk>/', views.PostDetailView.as_view(), name="detail"),

    
     
    
    # path('create/', views.PostCreateView.as_view(), name="post_create"),
    path('<int:pk>/edit/', views.PostEditView.as_view(), name="post_edit"),
    path('<int:pk>/delete/', views.PostDeletePost.as_view(), name="post_delete"),
   
    
  
]