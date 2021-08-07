from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User  # 작성자 가져옴(기본설정 되어있는 user를 가져온다)


class Photo(models.Model):  # model 받아옴
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_photos')  # user로 연결하고 삭제되면 같이 삭제되게 한다
    photo = models.ImageField(upload_to='photos/%Y/%m/%d',
                              default='photos/no_img.png')  # 디렉토리 찾는 창을 띄워주는 형식이다.포토 폴더안에 연도/월/날짜 를 만들어준다.
    # 없으면 no_img.png를 만들어줘서 오류를 방지해준다.
    text = models.TextField()  # 본문 적기

    created = models.DateTimeField(auto_now_add=True)  # 생성된 날짜, 자동으로 현재시간을 추가해준다.
    updated = models.DateTimeField(auto_now=True)  # 수정된 시간을 넣어준다.

    class Meta:
        ordering = ['-updated']  # 업데이트된 시각을 기준으로 정렬한다.(-는 내림차순 없으면 오름차순)

    def __str__(self):
        return self.author.username + " " + self.created.strftime("%Y-%m-%d")  # users안에 username이 있다.
    # 이름과 시간을 받아온다. 시 분 초가 대문자를 쓰고 나머지는 소문자로 쓴다

    def get_absolute_url(self):
        return reverse('photo:photo_detail', args=[str(self.id)])# 다시 넘겨준다
