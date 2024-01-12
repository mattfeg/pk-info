from django.urls import path, include
from .views import grid_page, contact_page, register_page, index_page

urlpatterns = [
    path('', index_page, name='index'),
    path('grid/', grid_page, name='grid'),
    path('contact/', contact_page, name='contact'),
    path('register/', register_page, name='register'),
]
