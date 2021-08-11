from decimal import Decimal
from django.conf import settings
from shop.models import Product
from coupon.models import Coupon


class Cart(object):
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_ID)  # config/settings.에 있는 session id를 cart에서 호출이되면 쓰겠다.
        if not cart:
            cart = self.session[settings.CART_ID] = {}

        self.cart = cart
        self.coupon_id = self.session.get('coupon_id')  # 세션에서 쿠폰 아이디만 가져온다.

    def __len__(self):  # 카트 갯수
        return sum(item['quantity'] for item in self.cart.values())  # 카트 담겨있는 각각 아이템들 몇개 주문했는지 가지고 와서 합한다.

    def __iter__(self):
        product_ids = self.cart.keys()  # 카트에있는 각각 키값
        products = Product.objects.filter(id__in=product_ids)

        for product in products:  # 있는것만큼 카트에 담아라
            self.cart[str(product.id)]['product'] = product

            # 데이터 베이스에 있는 목록중 카트에 담기로한 제품 목록을 하나씩 가지고 와서 로컬에 담고 그 담은걸 그냥 못쓰니까 세션에 담기(카트에 담기)

        for item in self.cart.values():
            item['price'] = Decimal(item['price'])  # 객체형태로 만드는것
            item['total_price'] = item['price'] * item['quantity']

            yield item

    def add(self, product, quantity=1, is_update=False):  # 1은 default값이다. 값이 없으면 한개이다.
        product_id = str(product.id)
        if product_id not in self.cart:  # pro아이디가 없으면
            self.cart[product_id] = {'quantity': 0, 'price': str(product.price)}

        if is_update:
            self.cart[product_id]['quantity'] = quantity
        else:
            self.cart[product_id]['quantity'] += quantity  # 카트에 담겨있는 아이템인데 똑같은걸 담으면 갯수가 추가된다.

        self.save()

    def save(self):
        self.session[settings.CART_ID] = self.cart
        self.session.modified = True

    def remove(self, product):
        product_id = str(product.id)
        if product_id in self.cart:
            del(self.cart[product_id])
            self.save()

    def clear(self):
        self.session[settings.CART_ID] = {}
        self.session.modified = True
        self.session['coupon_id'] = None  # 카트가 삭제되면 쿠폰아이디도 같이 삭제

    def get_product_total(self):
        return sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values())

    @property  # 데코레이터
    def coupon(self):
        if self.coupon_id:  # 쿠폰아이디가 있으면
            return Coupon.objects.get(id=self.coupon_id)  # 해당하는 쿠폰찾기
        return None  # 돌려주는건 필요없다(있을때만 가지고오면된다)

    def get_discount_total(self):
        if self.coupon:  # 쿠폰이 있고
            if self.get_product_total() >= self.coupon.amount:
                # 카트에 물건이 있어야하고 쿠폰가격보다 커야한다.
                return self.coupon.amount
        return Decimal(0)  # 계산식 위에 있음 쿠폰없으면 0을 넘겨준다. 있으면 쿠폰값 넘겨줌

    def get_total_price(self):
        return self.get_product_total() - self.get_discount_total()  # 최종 가격 표시

