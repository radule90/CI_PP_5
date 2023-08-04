from django.shortcuts import render, redirect
from .models import Contact
from django.contrib import messages
# Create your views here.


def contact(request):
    '''
    Function based view to handle contact message data from user
    '''
    if request.method == 'POST':
        contact = Contact()
        contact.full_name = request.POST.get('full_name')
        contact.email = request.POST.get('email')
        contact.subject = request.POST.get('subject')
        contact.message = request.POST.get('message')
        contact.save()
        messages.success(request, 'Your message has been sent successfully.')
        return redirect('contact')        
    template = 'contact/contact.html'
    context = {
        'active_contact': 'active_contact',
    }
    return render(request, template, context)
