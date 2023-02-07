from django.shortcuts import (render, redirect, reverse,
                              get_object_or_404, HttpResponse)
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.conf import settings

from .forms import OrderForm, Order
from .models import OrderLineItem
from products.models import Product
from bag.contexts import bag_contents

import stripe
import json


@require_POST
def cache_checkout_data(request):
    try:
        # split the payment intent id from the client secret
        pid = request.POST.get('client_secret').split('_secret')[0]
        stripe.api_key = settings.STRIPE_SECRET_KEY
        # add metadata of user, bag and if save info checked
        stripe.PaymentIntent.modify(pid, metadata={
            'bag': json.dumps(request.session.get('bag', {})),
            'save_info': request.POST.get('save_info'),
            'username': request.user,
        })
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, 'Sorry, your payment cannot be \
            processed right now. Please try again later.')
        return HttpResponse(content=e, status=400)


def checkout(request):
    """ Render checkout page with order form,
    create payment intent """

    # retrive stripe api keys
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.method == 'POST':
        # retrieve the bag from the session
        bag = request.session.get('bag', {})

        form_data = {
            'full_name': request.POST['full_name'],
            'email': request.POST['email'],
            'phone_number': request.POST['phone_number'],
            'country': request.POST['country'],
            'postcode': request.POST['postcode'],
            'town_or_city': request.POST['town_or_city'],
            'street_address1': request.POST['street_address1'],
            'street_address2': request.POST['street_address2'],
            'county': request.POST['county'],
        }

        order_form = OrderForm(form_data)

        if order_form.is_valid():
            order = order_form.save()
            # iterate through bag items to create line item
            for item_id, item_data in bag.items():
                try:
                    product = Product.objects.get(pk=item_id)
                    order_line_item = OrderLineItem(
                        order=order,
                        product=product,
                        quantity=item_data,
                    )
                    order_line_item.save()
                # give user error message if product not found
                except Product.DoesNotExist:
                    messages.error(request, (
                        "One of the products in your bag wasn't "
                        "found in our database. "
                        "Please call us for assistance!")
                    )
                    order.delete()
                    return redirect(reverse('view_bag'))

            # Save the info to the user's profile if box is ticked
            request.session['save_info'] = 'save-info' in request.POST
            # pass order number to checkout success page
            return redirect(reverse('checkout_success',
                                    args=[order.order_number]))
        else:
            messages.error(request, ('Form error, please check the'
                                     'information you have input.'))
    else:
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


def checkout_success(request, order_number):
    """ Page to handle successful checkout """

    # check if user requested to save delivery information
    save_info = request.session.get('save_info')

    # get the successful order number
    order = get_object_or_404(Order, order_number=order_number)
    # confirm success to user
    messages.success(request, f'Order successfully processed! \
        Your order number reference is {order_number}. A confirmation \
        email will be sent to {order.email}.')

    # clear bag
    if 'bag' in request.session:
        del request.session['bag']

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
    }

    return render(request, template, context)
