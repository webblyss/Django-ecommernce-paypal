from django.urls import path
from .views import home,add_to_cart

app_name = 'home'

urlpatterns = [
    path('',home,name="home"),
    path('add_to_cart/<int:product_id>/', add_to_cart, name='add_to_cart'),
]


 