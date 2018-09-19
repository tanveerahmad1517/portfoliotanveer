
from django.conf.urls import url
from .import views
# from posts.views import HomeView
from django.urls import path
# from account.views import profile
app_name = 'posts'

app_name = 'posts'
urlpatterns = [
    path('', views.AllPostList.as_view(), name="all"),
    # path('posts/', views.posts, name='all'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name="detail"),
    url(r'^(?P<username>[^/]+)/$', views.profile, name='profile'),
    path('create/', views.PostCreateView.as_view(), name="post_create"),
    path('<int:pk>/edit/', views.PostEditView.as_view(), name="post_edit"),
    path('<int:pk>/delete/', views.PostDeletePost.as_view(), name="post_delete"),
    # url(r'^(?P<username>[^/]+)/$', views.profile, name='profile'),

]