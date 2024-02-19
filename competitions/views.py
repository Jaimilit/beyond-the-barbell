from django.shortcuts import render


# Create your views here.


def competitions(request):
    """ A view to return the competitions page """

    return render(request, 'competitions.html')
