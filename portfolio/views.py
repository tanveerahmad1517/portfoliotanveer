from django.core.mail import EmailMessage
from django.shortcuts import render, redirect
from django.template.loader import get_template
from portfolio.forms import ContactForm
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