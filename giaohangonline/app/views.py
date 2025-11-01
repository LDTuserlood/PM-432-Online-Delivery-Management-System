from django.shortcuts import render,redirect
from django.http import HttpResponse
# Create your views here.
def home(request):
    if request.user.is_authenticated:
        customer = request.user
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
        user_not_login = "hidden" # và ẩn dk dn
        user_login = "show" #nếu đăng nhập thì hiện chào
    else:
        items =[]
        order = {'get_cart_items':0,'get_cart_total':0}
        cartItems = order['get_cart_items']
        user_not_login = "show" # ch đăng nhập thì hiện dk dn
        user_login = "hidden" # và ẩn chào 
   
    return render(request,'app/home.html')
