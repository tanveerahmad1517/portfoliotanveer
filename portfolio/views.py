from django.core.mail import EmailMessage
from django.shortcuts import render, redirect
from django.template.loader import get_template
from portfolio.forms import ContactForm
from gallery.models import Gallery_Category, Artwork
from blog.models import Post, Category
from django.db.models import Count
# our view
def contact(request):
    form_class = ContactForm

    # new logic!
    if request.method == 'POST':
        form = form_class(data=request.POST)

        if form.is_valid():
            contact_name = request.POST.get(
                'contact_name'
            , '')
            contact_email = request.POST.get(
                'contact_email'
            , '')
            form_content = request.POST.get('content', '')        
            template = get_template('contact_template.txt')
            context = {
                'contact_name': contact_name,
                'contact_email': contact_email,
                'form_content': form_content,
            }
            content = template.render(context)

            email = EmailMessage(
                "New contact form submission",
                content,
                "Your website" +'',
                ['adeelali.objects@gmail.com'],
                headers = {'Reply-To': contact_email }
            )
            email.send()
            return redirect('success')

    return render(request, 'contactus.html', {
        'form': form_class,
    })



def successView(request):
    return render(request, 'success.html')


def about_me(request):
    return render(request, 'about_me.html')




def home(request, category_slug=None, gcategory_slug=None):
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
    gcategory = None
    gcategories = Gallery_Category.objects.all()
    artwork = Artwork.objects.filter(available=True)
    if gcategory_slug:
        language = request.LANGUAGE_CODE
        gcategory = get_object_or_404(Gallery_Category,
                                     translations__language_code=language,
                                     translations__slug=gcategory_slug)
        artwork = artwork.filter(gcategory=gcategory)
    return render(request,
                  'home.html',
                  {'gcategory': gcategory,
                   'gcategories': gcategories,
                   'artwork': artwork,
                   'categories': categories,
                   'post': post
                })
