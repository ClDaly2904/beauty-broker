from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Product, Product_Category, Skin_Concern


def all_products(request):
    """ A view to show all products, including sorting and search queries """

    products = Product.objects.all()
    query = None
    product_type = None
    context = None
    sort = None
    direction = None

    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any"
                                        " search criteria!")
                return redirect(reverse('products'))

            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)
            context = {
                'products': products,
                'search_term': query,
            }

        if 'product_type' in request.GET:
            product_type = request.GET['product_type'].split(',')
            products = products.filter(product_type__name__in=product_type)
            categories = Product_Category.objects.filter(name__in=product_type)
            context = {
                'products': products,
                'current_category': categories,
            }

        if 'skin_type' in request.GET:
            skin_type = request.GET['skin_type'].split(',')
            products = products.filter(skin_type__name__in=skin_type)
            skin_concern_category = Skin_Concern.objects.filter(name__in=skin_type)
            context = {
                'products': products,
                'current_skin_concern': skin_concern_category,
            }

        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)
            current_sorting = f'{sort}_{direction}'
            context = {
                'products': products,
                'current_sorting': current_sorting,
            }

        else:
            context = {
                'products': products,
            }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ A view to show details for a specific product """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)
