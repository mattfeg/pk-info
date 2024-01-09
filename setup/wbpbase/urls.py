from django.urls import path, include
from setup.wbpbase import views

urlpatterns = [
    path('', views.index_page, name='index'),
    path('grid/', views.grid_page, name='grid'),
    path('contact/', views.contact_page, name='contact'),
    path('register/', views.register_page, name='register'),
]
