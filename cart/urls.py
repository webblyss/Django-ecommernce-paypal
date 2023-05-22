from django.urls import path
from .views import cart,delete_cart,add_quantity,decrease_quantity



app_name = "cart"
urlpatterns = [
        path('',cart,name='cart'),
        path('delete_cart/<int:product_id>/',delete_cart,name='delete_cart'),
        path('add_qauntity/<int:product_id>/',add_quantity,name="add_qauntity"),
        path('decrease_quantity/<int:product_id>/',decrease_quantity,name="decrease_quantity")
]





