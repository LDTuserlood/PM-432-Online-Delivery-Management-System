from django.shortcuts import render,redirect
from django.http import HttpResponse
# Create your views here.
from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from .models import *
import json
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from django.contrib import messages
from django.shortcuts import render, redirect
from .models import ShippingAddress, Order
from django.core.mail import send_mail
from webbanhang.settings import EMAIL_HOST_USER
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_decode
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Order, ShippingAddress
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Order, OrderItem
from django.shortcuts import render
from .models import Order  # Import model Order nếu chưa có
from django.core.paginator import Paginator  # Import phân trang nếu cần
from django.shortcuts import render, redirect, get_object_or_404
from .models import Order, Customer
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.contrib import messages


from django.shortcuts import render
from .models import Order  # Đảm bảo import model Order
from django.shortcuts import render, redirect
from app.models import Order, OrderDetail
from django.shortcuts import render, redirect
from app.models import Order, OrderDetail, Product
from django.shortcuts import get_object_or_404, redirect
from .models import Order
from django.shortcuts import get_object_or_404
from .forms import CreateUserForm



def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    # 🔥 Kiểm tra số lượng đơn chưa hoàn thành của user
    max_orders = 3  # Giới hạn số đơn chưa hoàn thành
    pending_orders = Order.objects.filter(customer=request.user, complete=False).count()

    if pending_orders >= max_orders:
        messages.error(request, "Bạn đã đạt giới hạn đơn hàng chưa hoàn thành. Vui lòng hoàn thành đơn trước khi đặt thêm!")
        return redirect('cart')  # Chuyển hướng về giỏ hàng

    # 🔥 Nếu chưa đạt giới hạn, tiếp tục tạo đơn
    order, created = Order.objects.get_or_create(customer=request.user, complete=False)

    order_item, item_created = OrderItem.objects.get_or_create(order=order, product=product)
    order_item.quantity += 1
    order_item.save()

    messages.success(request, "Sản phẩm đã được thêm vào giỏ hàng.")
    return redirect('cart')
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
