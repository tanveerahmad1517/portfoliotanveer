from django.shortcuts import render

from django.shortcuts import render, get_object_or_404
import json
from django_ajax.decorators import ajax
# Create your views here.
from .models import Post, Category
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from braces.views import LoginRequiredMixin
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from . import forms

# class AllPostList(ListView):
#     model = Post
#     context_object_name = 'post'
#     paginate_by = 4


def profile(request, username):
    page_user = get_object_or_404(User, username=username)
    posts = Post.objects.filter(user=page_user)
    data = {
        'page_user': page_user,

        'posts': posts,
    }

    return render(request, 'blog/profile.html', data)



def post_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    post = Post.objects.filter(available=True)
    if category_slug:
        language = request.LANGUAGE_CODE
        category = get_object_or_404(Category,
                                     translations__language_code=language,
                                     translations__slug=category_slug)
        post = post.filter(category=category)
    return render(request,
                  'blog/_post.html',
                  {'category': category,
                   'categories': categories,
                   'post': post})



# class PostDetailView(DetailView):
#     model = Post
#     template_name = 'blog/detail.html'

def detail(request, id, slug):
    language = request.LANGUAGE_CODE
    post = get_object_or_404(Post,
                                id=id,
                                translations__language_code=language,
                                translations__slug=slug,
                                available=True)
    # cart_product_form = CartAddProductForm()

    # r = Recommender()
    # recommended_products = r.suggest_products_for([product], 4)

    return render(request,
                  'blog/detail.html',
                  {'post': post,
                  # 'cart_product_form': cart_product_form,
                  # 'recommended_products': recommended_products 
                })






class PostEditView(UpdateView):
    model = Post
    fields = '__all__'
    template_name = 'blog/post_edit.html'

class PostDeletePost(DeleteView):
    model = Post
    success_url = reverse_lazy("posts:all")


# class PostCreateView(LoginRequiredMixin, CreateView):
#     form_class = forms.TweetModelForm
#     model = Post
#     # fields = '__all__'
#     template_name = 'posts/post_create.html'





