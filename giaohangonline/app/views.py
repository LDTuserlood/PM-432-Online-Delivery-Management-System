from django.shortcuts import render


# Create your views here.
def placeorder(request):
    if request.method == "POST":
        customer = request.user if request.user.is_authenticated else None
        name = request.POST.get('name')
        mobile = request.POST.get('phone')
        email = request.POST.get('email')
        address = request.POST.get('address')
        city = request.POST.get('city')
        district = request.POST.get('district')
        ward = request.POST.get('ward')
        
        shipping_address = ShippingAddress.objects.create(
            customer=customer,
            name = name,
            mobile=mobile,
            email=email,
            address=address,
            city=city,
            district=district,
            ward=ward
        )
    if request.user.is_authenticated:
        customer = request.user
        order, created = Order.objects.get_or_create(customer = customer, complete = False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
        user_not_login = "hidden"
        user_login = "show"
    else:
        items =[]
        order = {'get_cart_items':0,'get_cart_total':0}
        cartItems = order['get_cart_items']
        user_not_login = "show"
        user_login = "hidden"
    menus = Menu.objects.filter(is_sub=False)
    context={'menus':menus,'items':items,'order':order,'cartItems': cartItems,'user_not_login':user_not_login,'user_login':user_login}
    return render(request,'app/placeorder.html',context)
def home(request):
    if request.user.is_authenticated:
        customer = request.user
        order, created = Order.objects.get_or_create(customer = customer, complete = False)
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
    menus = Menu.objects.filter(is_sub=False)
    products = Product.objects.all()
    context={'menus':menus,'products': products,'cartItems': cartItems,'user_not_login':user_not_login,'user_login':user_login}
    return render(request,'app/home.html',context)
