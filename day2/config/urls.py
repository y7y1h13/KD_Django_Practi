from django.contrib import admin
from django.urls import path, include

from django.conf.urls.static import static #고정파일 불러오기
from django.conf import settings



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('photo.urls')),  # 바로들어가짐, photo.urls로 길 안내를 해준다.
    path('accounts/', include('accounts.urls')),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)#static에 관련된것만 붙여줘!
