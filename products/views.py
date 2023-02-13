from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower

from .models import Product, Product_Category, Skin_Concern, Brand
from .forms import ProductForm


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

            queries = (Q(name__icontains=query) |
                       Q(description__icontains=query))
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
                'product_type': product_type,
            }

        if 'skin_type' in request.GET:
            skin_type = request.GET['skin_type'].split(',')
            products = products.filter(skin_type__name__in=skin_type)
            sc_word = "".join(skin_type)
            skin_concern_category = sc_word.replace('_', ' ')
            context = {
                'products': products,
                'skin_type': skin_concern_category,
            }

        if 'sort' in request.GET:
            sortkey = request.GET['sort']

            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))

            if sortkey == 'product_type':
                sortkey = 'product_type__name'

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


@login_required
def add_product(request):
    """ A view for store owners to add a product """

    # prevent unauthorised users from product management
    if not request.user.is_superuser:
        messages.error(request, "Sorry, you're not authorised to do that.")
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('add_product'))
        else:
            messages.error(request, 'Failed to add product. Please ensure\n'
                                    'the information provided is valid.')
            return render(request, 'products/add_product.html', {'form': form})
    else:
        form = ProductForm()
    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_product(request, product_id):
    """ A view for store owners to edit an existing product """

    # prevent unauthorised users from product management
    if not request.user.is_superuser:
        messages.error(request, "Sorry, you're not authorised to do that.")
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)

    if request.method == 'POST':

        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated product!')
            # return user to the newly updated product page
            return redirect(reverse('product_detail', args=[product.pk]))
        else:
            messages.error(request, 'Failed to update product information.\n'
                                    ' Please ensure the information provided\n'
                                    'is valid.')

    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    template = 'products/edit_product.html'
    context = {
        'product': product,
        'form': form,
    }

    return render(request, template, context)


@login_required
def delete_product(request, product_id):
    """ Delete a product from the store """

    # prevent unauthorised users from product management
    if not request.user.is_superuser:
        messages.error(request, "Sorry, you're not authorised to do that.")
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)

    if request.method == 'POST':
        product.delete()
        messages.success(request, 'Product deleted!')
        return redirect(reverse('products'))

    template = 'products/delete_product.html'
    context = {
        'product': product,
    }
    return render(request, template, context)


def brand_page(request, brand_id):
    """ A view for displaying information for the
    ordinary featured brand """

    products = Product.objects.filter(brand=brand_id)
    brand = get_object_or_404(Brand, pk=brand_id)

    template = 'products/brand_page.html'
    context = {
        'products': products,
        'brand': brand,
    }
    return render(request, template, context)
