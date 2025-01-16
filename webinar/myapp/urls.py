from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('definicje/', views.definicje, name='definicje'),
    path('postepowanie/', views.postepowanie, name='postepowanie'),
    path('ustawy/', views.ustawy, name='ustawy')
]
