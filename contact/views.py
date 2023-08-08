from django.shortcuts import render, redirect
from .models import Contact
from django.contrib import messages
# Create your views here.


def contact(request):
    '''
    Function based view to handle contact message data from user
    '''
    if request.method == 'POST':
        # On post request create new instance
        contact = Contact()
        # Fetch all data from post request
        contact.full_name = request.POST.get('full_name')
        contact.email = request.POST.get('email')
        contact.subject = request.POST.get('subject')
        contact.message = request.POST.get('message')
        # Save instance, send successfull message, redirect bact to contact
        contact.save()
        messages.success(request, 'Your message has been sent successfully.')
        return redirect('contact')
    template = 'contact/contact.html'
    context = {
        'active_contact': 'active_contact',
    }
    return render(request, template, context)
