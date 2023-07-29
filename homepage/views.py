from django.shortcuts import render

# Create your views here.


def homepage(request):
    template = 'homepage/index.html'
    context = {}
    return render(request, template, context)
