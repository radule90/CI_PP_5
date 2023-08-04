from django.shortcuts import render

# Create your views here.


def contact(request):
    template = 'contact/contact.html'
    context = {
        'active_contact': 'active_contact',
    }
    return render(request, template, context)