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
from django.db .models import Count
import re
from account.models import Profile
from django.db.models import Q
from gallery.models import Artwork, Gallery_Category

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



class post_list(ListView):
  def get(self, request, category_slug=None):
    category = None
    categories = Category.objects.all().prefetch_related('category')
    categories = categories.annotate(post=Count('category'))
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

# def post_list(request, category_slug=None):
#     category = None
#     categories = Category.objects.all()
#     post = Post.objects.filter(available=True)
#     if category_slug:
#         language = request.LANGUAGE_CODE
#         category = get_object_or_404(Category,
#                                      translations__language_code=language,
#                                      translations__slug=category_slug)
#         post = post.filter(category=category)
#     return render(request,
#                   'blog/_post.html',
#                   {'category': category,
#                    'categories': categories,
#                    'post': post})



# class PostDetailView(DetailView):
#     model = Post
#     template_name = 'blog/detail.html'

# def detail(request, id, slug):
#     language = request.LANGUAGE_CODE
#     post = get_object_or_404(Post,
#                                 id=id,
#                                 translations__language_code=language,
#                                 translations__slug=slug,
#                                 available=True)
#     # cart_product_form = CartAddProductForm()

#     # r = Recommender()
#     # recommended_products = r.suggest_products_for([product], 4)

#     return render(request,
#                   'blog/detail.html',
#                   {'post': post,
#                   # 'cart_product_form': cart_product_form,
#                   # 'recommended_products': recommended_products 
#                 })


import random
class detail(DetailView):
  model = Post
  template_name = 'blog/detail.html'
  pk_url_kwarg = "id"
  pk_url_kwargs = "slug"
  # slug_field = "id" 
  # query_pk_and_slug = True
  def get_context_data(self, *args, **kwargs):
    context = super(detail, self).get_context_data(*args, **kwargs)
    instance = self.get_object()
        #order_by("-title")
    context["related"] = sorted(Post.objects.get_related(instance)[:6], key= lambda x: random.random())
    return context
    # cart_product_form = CartAddProductForm()

    # r = Recommender()
    # recommended_products = r.suggest_products_for([product], 4)

    # return render(request,
    #               'blog/detail.html',
    #               {'post': post,
    #               # 'cart_product_form': cart_product_form,
    #               # 'recommended_products': recommended_products 
    #             })
    # model = Post

    # # context_object_name = 'instance'
    # template_name = 'blog/detail.html'

    # #template_name = "<appname>/<modelname>_detail.html"
    # def get_context_data(self, request, id, s *args, **kwargs):
    #     context = super(detail, self).get_context_data(*args, **kwargs)
    #     instance = self.get_object()
    #     #order_by("-title")
    #     context["related"] = sorted(Post.objects.get_related(instance)[:6], key= lambda x: random.random())
    #     return context


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









def search(request):
    query = request.GET.get('search')
    if str(query) is '':
        return HttpResponseRedirect('/')
    pat = re.compile(r'[@](\w+)')
    attags = pat.finditer(query)
    search_profile = None
    for attag in attags:
        try:
            search_profile = User.objects.get(username = attag.group()[1:])
            return HttpResponseRedirect('/accounts/profile/user/%s'%search_profile.username)
        except ObjectDoesNotExist:
            search_profile = None
        break
    
    search_data = Post.objects.filter(Q(title__icontains=query) |
                                      Q(description__icontains=query))
    search_dataa = Category.objects.filter(Q(translations__name__icontains=query) 
                                          

      )
    people = User.objects.filter(first_name__icontains=query).order_by('-first_name')
    artwork_data = Artwork.objects.filter(Q(title__icontains=query) |
                                          Q(description__icontains=query)
      )
    artworkcat_data = Gallery_Category.objects.filter(Q(translations__name__icontains=query)
                                          
      )
    return render(request, 'blog/search_results.html', {'search_data':search_data, 'search_dataa':search_dataa, 'query':query, 'search_profile':search_profile, 'people': people, 'artwork_data':artwork_data})
    #We can differenitate here on the basis of the search query we have got like @ and # or any other textual query
