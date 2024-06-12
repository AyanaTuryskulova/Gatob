from django.urls import path
from . import views

urlpatterns = [
    path('', views.gallery, name='gallery'),
    path('photo/<str:pk>/', views.viewPhoto, name='photo'),
    path('add/', views.addPhoto, name='add'),
    path('registration/', views.registration_view, name='registration'),
    path('gatob/', views.gatob, name='gatob'),
    
]