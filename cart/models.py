from django.db import models
from django.contrib.auth.models import User
from django.db import models

from home.models import Product



class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    
    def __str__(self) -> str:
        return f'{self.product.title}~{self.cart.user.username}'
