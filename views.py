from django.shortcuts import render

# Create your views here.


def home(request):

    context = {}
    return render(request, 'accounts/home.html', context)
