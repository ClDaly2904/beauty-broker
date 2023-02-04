from django.shortcuts import render, redirect, get_object_or_404, reverse
from products.models import Product


# Create your views here.
def view_bag(request):
    """ A view to render the users shopping bag page """

    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """ Add a specified quantity of the product
    to the users shopping bag """

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if item_id in list(bag.keys()):
        bag[item_id] += quantity

    else:
        bag[item_id] = quantity

    request.session['bag'] = bag
    return redirect(redirect_url)


def update_bag(request, item_id):
    """Adjust quantity of a particular product to the specified amount"""

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))

    bag = request.session.get('bag', {})

    if quantity > 0:
        bag[item_id] = quantity

    else:
        bag.pop(item_id)

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))
