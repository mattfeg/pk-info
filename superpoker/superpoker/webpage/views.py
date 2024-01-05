from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'template/index.html')


def register(request):
    return render(request, 'template/register.html')


def contact(request):
    return render(request, 'template/contact.html')


def grid(request):
    return render(request, 'template/grid.html')


