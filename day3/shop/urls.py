from django.urls import path
from .views import *

app_name = 'shop'#앱 네임

urlpatterns = [
    path('', product_in_category, name='product_all'),
    path('<slug:category_slug>/', product_in_category, name='product_in_category'),
    path('<int:id>/<product:slug>/', product_detail, name='product_detail')#슬러그를 받을수도있고 안받을수도있다.


]