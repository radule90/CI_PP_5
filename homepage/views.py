from django.shortcuts import render

# Create your views here.


def homepage(request):
    template = 'homepage/index.html'
    context = {
        'active_homepage': 'active_homepage',
    }
    return render(request, template, context)
