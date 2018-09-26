from django.shortcuts import render, get_object_or_404
import json
from django_ajax.decorators import ajax
# Create your views here.
from blog.models import Post
from account.models import  Profile
from django.views.generic import ListView, DetailView
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.views.generic.edit import CreateView, UpdateView, View
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
# from account.forms import UserEditForm, ProfileEditForm
from django.contrib import messages


posts_NUM_PAGES = 10
@login_required(login_url='/login/')
def profile(request, username):
    page_user = get_object_or_404(User, username=username)
    all_posts = Post.objects.filter(user=page_user)
    paginator = Paginator(all_posts, posts_NUM_PAGES)
    post = paginator.page(1)
    from_Post = -1
    if posts:  # pragma: no cover
        from_Post = posts[0].id

    Posts_count = Post.objects.filter(user=page_user).count()
    data = {
        'page_user': page_user,
       
        
      
        'bar_data': [
            Posts_count],
        'bar_labels': json.dumps('["Posts"]'),  # noqa: E501

        'posts': posts,
        'from_Post': from_Post,
        'page': 1
        }
   
    return render(request, 'blog/profile.html', data)
