from django.urls import path

from . import views

app_name = 'pizza_app'
urlpatterns = [
    path('', views.index, name='index'),
    path('pizza_page/', views.pizza_page, name='pizza_page'),
    path('side_page/', views.side_page, name= 'side_page'),
    path('drink-page/', views.drink_page, name='drink_page'),
]