from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from checkout.models import Order
from .forms import UserProfileForm
from .models import UserProfile


@login_required
def profile(request):
    """ Display the user profile information """

    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account information\n'
                                      'successfully updated')
        else:
            messages.error(request,
                           ('Could not update account information.\n'
                            'Please check form for errors.'))
    else:
        form = UserProfileForm(instance=profile)
    orders = profile.orders.all()

    template = 'profiles/profile.html'
    context = {
        'form': form,
        'profile': profile,
        'orders': orders,
        'on_profile_page': True
    }

    return render(request, template, context)


def order_history(request, order_number):
    """ Get the details of a particular past order """

    order = get_object_or_404(Order, order_number=order_number)

    # remind user this is a past order
    messages.info(request, (
        f'This is a past confirmation for order number {order_number}.\n'
        'Please check your email inbox for the order confirmation\n'
        'sent on the day.'
    ))

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'from_profile': True,
    }

    return render(request, template, context)
