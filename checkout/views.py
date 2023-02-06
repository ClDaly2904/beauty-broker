from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.conf import settings

from .forms import OrderForm
from bag.contexts import bag_contents

import stripe


def checkout(request):
    """ Render checkout page with order form """

    # retrive stripe api keys
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    # retrieve the bag from the session
    bag = request.session.get('bag', {})

    # prevent url from being accessed manually if bag empty
    if not bag:
        messages.error(request, "Sorry, your bag is empty!")
        return redirect(reverse('products'))

    # get bag total as int for stripe to make charges
    current_bag = bag_contents(request)
    total = current_bag['grand_total']
    stripe_total = round(total * 100)
    stripe.api_key = stripe_secret_key
    # create payment intent
    intent = stripe.PaymentIntent.create(
        amount=stripe_total,
        currency=settings.STRIPE_CURRENCY,
    )

    # create instance of order form
    order_form = OrderForm()

    # set alert if public key not set
    if not stripe_public_key:
        messages.warning(request, ('Stripe public key missing! '
                                   'Is it set in your environment?'))

    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }

    return render(request, template, context)
