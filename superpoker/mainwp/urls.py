from django.urls import path
from mainwp.views import index_page, register_page, grid_page, contact_page

urlpatterns = [
    path('', index_page, name="index"),
    path('register/', register_page, name="register"),
    path('grid/', grid_page, name="grid"),
    path('contact/', contact_page, name="contact"),
]
