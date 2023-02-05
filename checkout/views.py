from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .forms import OrderForm


def checkout(request):
    """ Render checkout page with order form """

    # retrieve the bag from the session
    bag = request.session.get('bag', {})

    # prevent url from being accessed manually if bag empty
    if not bag:
        messages.error(request, "Sorry, your bag is empty!")
        return redirect(reverse('products'))

    # create instance of order form
    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
    }

    return render(request, template, context)
