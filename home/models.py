from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    image = models.ImageField(upload_to="pics")
    description = models.TextField()
    offer = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)
    
    
    
    def __str__(self) -> str:
        return f'{self.title}~{self.user.username}'
    


# UPDATE TOTAL CART IN DATABASE


class TotalCart(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    total_carts = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return f'{self.user.username} ~ {self.total_carts}'
 



