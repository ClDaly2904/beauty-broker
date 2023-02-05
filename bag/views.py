from django.shortcuts import (render, redirect, get_object_or_404,
                              reverse, HttpResponse)
from django.contrib import messages
from products.models import Product


# Create your views here.
def view_bag(request):
    """ A view to render the users shopping bag page """

    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """ Add a specified quantity of the product
    to the users shopping bag """

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if item_id in list(bag.keys()):
        bag[item_id] += quantity
        messages.success(request, f'Updated {product.name} quantity to\n'
                                  f'{bag[item_id]}!')

    else:
        bag[item_id] = quantity
        messages.success(request, f'Added {product.name} to\n'
                                  'your shopping bag!')

    request.session['bag'] = bag
    return redirect(redirect_url)


def update_bag(request, item_id):
    """Adjust quantity of a particular product to the specified amount"""

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))

    bag = request.session.get('bag', {})

    if quantity > 0:
        bag[item_id] = quantity
        messages.success(request, f'Updated {product.name} quantity to\n'
                                  f'{bag[item_id]}!')

    else:
        bag.pop(item_id)
        messages.success(request, f'Successfully removed {product.name}\n'
                                  'from bag!')

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))


def remove_from_bag(request, item_id):
    """Remove item from bag"""

    try:
        bag = request.session.get('bag', {})
        product = get_object_or_404(Product, pk=item_id)

        bag.pop(item_id)
        messages.success(request, f'Successfully removed {product.name}\n'
                                  'from bag!')

        request.session['bag'] = bag
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)
