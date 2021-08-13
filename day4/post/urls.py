from django.urls import path
from .views import *

app_name = 'post'

urlpatterns = [
    path('', post_list, name='post_list'),
    path('detail/<int:id>/', post_detail, name='post_detail'),
]