from django.shortcuts import render,redirect
from .models import Product,TotalCart
# Create your views here.
from django.contrib.auth.decorators import login_required

from cart.models import Cart, CartItem


def  home(request):
    product  = Product.objects.all()

    return render(request,'index.html',{"product":product,})


@login_required
def add_to_cart(request, product_id):
    product = Product.objects.get(pk=int(product_id))
    cart, _ = Cart.objects.get_or_create(user=request.user)
    CartItem.objects.create(cart=cart, product=product)
    print('Item added successfully')
    
    # UPDATE CART TOTAL
    carts = CartItem.objects.all()
    data = list()
    for cart_ in carts:
        if cart_.cart.user.username == request.user.username:
            data.append(cart_)
            print(cart_)
            # UPDATE CART
    
    cart_count = len(data)
    
    
    
    return redirect('/')








