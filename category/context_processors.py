from .models import Category

def category_links(request):
    '''
    Context processor to add category links to the context of every template.
    '''
    links = Category.objects.all()
    return dict(links=links)