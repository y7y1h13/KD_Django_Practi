from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST

from shop.models import Product
from .forms import AddProductForm
from .cart import Cart
from coupon.forms import AddCouponForm  # 앱을 가져온다.


@require_POST  # 이게 있으면 포스트 있으면 아래가 실행이된다.
def add(request, product_id):  # id 호출받으면 카트에담는다
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)

    form = AddProductForm(request.POST)
    if form.is_valid():  # 값이 있으면
        cd = form.cleaned_data  # 한번 비우고
        cart.add(product=product, quantity=cd['quantity'], is_update=cd['is_update'])  # 추가한다(cart.py에 있는 내용)

    return redirect('cart:detail')  # 여기로 연결


def remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)  # 해당되는것만 삭제
    return redirect('cart:detail')


def detail(request):
    cart = Cart(request)
    add_coupon = AddCouponForm()

    for product in cart:
        product['quantity_form'] = AddProductForm(initial={  # add를 실행할때  받을값
            'quantity': product['quantity'], 'is_update': True
        })

    return render(request, 'cart/detail.html', {'cart': cart, 'add_coupon': add_coupon})
    # ''안에있는건 이런 이름으로 쓰겠다는 뜻(html안에서)