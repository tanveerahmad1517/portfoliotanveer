from django.shortcuts import render, get_object_or_404
from .models import Gallery_Category, Artwork, Subscribe


from blog.utils import SendSubscribeMail
from django.http import HttpResponse, JsonResponse
# def galleries(request):
#     gallery_groups = GalleryGroup.objects.all().order_by('title')
#     return render(request, 'gallery/galleries.html', {'galleryGroups': gallery_groups})


def artwork_list(request, gcategory_slug=None):
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
                  'gallery/galleries.html',
                  {'gcategory': gcategory,
                   'gcategories': gcategories,
                   'artwork': artwork})





def gallery_detail(request, pk):
    context_dict = {}
    
    try:
        gallery_groups = Gallery_Category.objects.get(pk=pk)
        context_dict['gcategory'] = gallery_groups
        artworks = Artwork.objects.filter(gcategory=gallery_groups).order_by('published_date')
        context_dict['artworks'] = artworks

    except Gallery_Category.DoesNotExist:
        pass

    return render(request, 'gallery/gallery_detail.html', context_dict)


def art_detail(request, art_id):
    artwork = get_object_or_404(Artwork, id=art_id)
    try:
        next_artwork = artwork.get_next_by_published_date()
        while next_artwork.gcategory != artwork.gcategory:
            next_artwork = next_artwork.get_next_by_published_date()
    except Artwork.DoesNotExist:
        next_artwork = None

    try:
        previous = artwork.get_previous_by_published_date()
        while previous.gcategory != artwork.gcategory:
            previous = previous.get_previous_by_published_date()
    except Artwork.DoesNotExist:
        previous = None

    return render(request, 'gallery/art_detail.html', {'artwork': artwork, 'next': next_artwork, 'previous': previous})




def subscribe(request):
    if request.method == 'POST':
        email = request.POST['email_id']
        email_qs = Subscribe.objects.filter(email_id = email)
        if email_qs.exists():
            data = {"status" : "404"}
            return JsonResponse(data)
        else:
            Subscribe.objects.create(email_id = email)
            SendSubscribeMail(email) # Send the Mail, Class available in utils.py
    return HttpResponse("/")