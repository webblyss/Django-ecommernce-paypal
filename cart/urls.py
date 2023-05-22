from django.urls import path
from .views import cart,delete_cart



app_name = "cart"
urlpatterns = [
        path('',cart,name='cart'),
        path('delete_cart/<int:product_id>/',delete_cart,name='delete')
]





