from django.urls import path
from .views import * #대문자로 넘어오면 클래스 소문자는 메소드


app_name = 'coupon'

urlpatterns = [
    path('add/', add_coupon, name='add'),




]
