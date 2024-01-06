from django.shortcuts import render

# Create your views here.
def index_page(request):
    return render(request, "mainwp/index.html")

def register_page(request):
    return render(request, "mainwp/register.html")

def grid_page(request):
    return render(request, "mainwp/grid.html")

def contact_page(request):
    return render(request, "mainwp/contact.html")