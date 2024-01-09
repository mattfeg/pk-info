from django.shortcuts import render

# Create your views here.
def index_page(request):
    return render(request, 'wbpbase/index.html')

def grid_page(request):
    return render(request, 'wbpbase/grid.html')

def contact_page(request):
    return render(request, 'wbpbase/contact.html')

def register_page(request):
    return render(request, 'wbpbase/register.html')