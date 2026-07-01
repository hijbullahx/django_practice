from django.urls import path
from .import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('login/', views.login, name = 'login'),
    path('contact/', views.contact, name  = 'contact'),
    path('features/', views.features, name = 'features'),
]