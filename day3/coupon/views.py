from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from django.utils import timezone  # 시간 가져오기

from .models import *
from .forms import AddCouponForm


@require_POST
def add_coupon(request):  # 쿠폰 추가(user가 쿠폰번호 입력하고 쓰겠다고 할 때 호출)
    now = timezone.now()  # 쓰는시간 알아내기
    form = AddCouponForm(request.POST)  # 폼에 값이 들어오게된다
    if form.is_valid():  # 값이 있으면
        code = form.cleaned_data['code']  # 코드로 초기화

        try:
            coupon = Coupon.objects.get(code__iexact=code, use_from__lte=now, use_to__gte=now, activate=True)
            # 코드가 입력될때 대소문자 무시하고, 쿠폰의 유효기간이 지금시간보다 커야함
            request.session['coupon_id'] = coupon.id  # 이걸받아서 저장해놓겠다.(카트리스트에 적용을 시켜놓는다)
            # 쿠폰을 쓸건데 쓰기전에 미리 가격을 보여준다.

        except Coupon.DoesNotExist:  # 쿠폰을 못찾았을때
            request.session['coupon_id'] = None  # 없음으로 처리해서오류를 없앤다.

        return redirect('cart:detail')#앱네임을 cart라고 해놨다. cart의 detail로 넘겨라






