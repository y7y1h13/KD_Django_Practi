from django.urls import path
from django.views.generic.detail import DetailView

from .views import *  # 다불러옴
from .models import Photo

app_name = 'photo'

urlpatterns = [
    path('', photo_list, name='photo_list'),  # 없으면 photo_list 호출
    path('detail/<int:pk>', DetailView.as_view(model=Photo, template_name='photo/detail.html'), name='photo_detail'),
    # 안만들고 바로씀, 그대신 형식 적어줘야함
    path('upload/', PhotoUploadView.as_view(), name='photo_upload'),  # view에서 정의한거 그대로씀
    path('delete/<int:pk>', PhotoDeleteView.as_view(), name='photo_delete'),
    path('update/<int:pk>', PhotoUpdateView.as_view(), name='photo_update'),

]
