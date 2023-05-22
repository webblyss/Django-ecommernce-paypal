from django.shortcuts import render,redirect,get_object_or_404
from .models import CartItem
from django.http import HttpResponseRedirect
# Create your views here.



def cart(request):
    carts = CartItem.objects.all()
    data = list()
    for cart_ in carts:
        if cart_.cart.user.username == request.user.username:
            data.append(cart_)
            print(cart_)
    
        
    return render(request,'cart.html',{"cart":data})




def delete_cart(request,product_id):
    cart_item = get_object_or_404(CartItem, id=product_id)
    cart_item.delete()
    print('item deleted successfully')
    return redirect('cart')


def addQuantity(request,pk):
    
    
    return



