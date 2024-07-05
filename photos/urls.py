from django.urls import path
from . import views
from .views import gallery, news_detail, like_news, add_comment,  register, user_login, user_logout


urlpatterns = [
    path('', views.gallery, name='gallery'),
    path('photo/<str:pk>/', views.viewPhoto, name='photo'),
    path('add/', views.addPhoto, name='add'),
    path('registration/', views.registration_view, name='registration'),
    path('photo/<int:pk>/', views.photo_detail, name='photo_detail'),
    path('photo/<int:pk>/like/', views.like_photo, name='like_photo'),
    path('photo/<int:pk>/comment/', views.add_comment, name='add_comment'),
    path('', gallery, name='gallery'),
    path('news/<int:pk>/', news_detail, name='news_detail'),
    path('news/<int:pk>/like/', like_news, name='like_news'),
    path('news/<int:pk>/comment/', add_comment, name='add_comment'),
    path('', gallery, name='gallery'),
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    
    
]
