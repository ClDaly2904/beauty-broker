from django.shortcuts import render, get_object_or_404
from django.contrib import messages

from .forms import UserProfileForm
from .models import UserProfile


# Create your views here.
def profile(request):
    """ Display the user profile information """

    profile = get_object_or_404(UserProfile, user=request.user)
    form = UserProfileForm(instance=profile)
    orders = profile.orders.all()

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
        'on_profile_page': True,
    }

    return render(request, template, context)
