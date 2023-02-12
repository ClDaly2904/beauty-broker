from django.shortcuts import render, get_object_or_404
from products .models import Brand

# Create your views here.


def index(request):
    """ A view to return the index page """

    brands = Brand.objects.all()
    the_ordinary = brands.filter(name='the_ordinary')
    glossier = brands.filter(name='glossier')

    template = 'home/index.html'

    context = {
        glossier: 'glossier',
        the_ordinary: 'the_ordinary'
    }

    return render(request, template, context)


def newsletter(request):
    """ A view to return the newsletter page """

    template = 'home/newsletter.html'

    context = {
    }

    return render(request, template, context)
