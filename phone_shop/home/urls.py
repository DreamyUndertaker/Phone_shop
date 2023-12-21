from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('catalog', views.catalog, name='catalog'),
    path('about', views.about, name='about'),
    path('shipping', views.shipping, name='shipping'),
    path('blog', views.blog, name='blog'),
    path('contacts', views.contacts, name='contacts')
]