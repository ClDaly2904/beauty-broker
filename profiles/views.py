from django.shortcuts import render


# Create your views here.
def profile(request):
    """ Display the user profile information """

    template = 'profiles/profile.html'
    context = {}

    return render(request, template)
