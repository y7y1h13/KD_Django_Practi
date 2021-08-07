from django.contrib import admin
from .models import * #같은 폴더에 있으면 .만 붙이면된다. 아니면 경로 써줘야함... *은 전체다 불러옴
# Register your models here.


class PhotoAdmin(admin.ModelAdmin):
    list_display = ['id', 'author', 'created', 'updated']#리스트를 어떻게 표현할것인가
    raw_id_fields = ['author']#기준 id
    list_filter = ['created', 'updated', 'author']#단어들이 떠서 검색하기 편함(필터로 쓸 값들)
    search_fields = ['text', 'created'] #본문과 생성일 기준으로 검색
    ordering = ['-updated', '-created'] #정렬기준은 -(내림차순) 업데이트날짜와 생성 날짜




admin.site.register(Photo, PhotoAdmin)#admin에 photo의 데이터를 등록해줬다.///만든걸 적용해야한다.
