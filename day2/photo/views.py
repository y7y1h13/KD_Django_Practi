from django.shortcuts import render, redirect  # 다시 주소 돌려주는거 호출
from django.views.generic.edit import CreateView, DeleteView, UpdateView  # 기능 호출
from .models import Photo


class PhotoUploadView(CreateView):  # 생성되는 페이지를 직접 작성하지 않고 장고에서 생성된거로 쓴다
    model = Photo
    fields = ['photo', 'text']  # 입력은 포토와 텍스트를 가져온다
    template_name = 'photo/upload.html'  # 여기랑 연결시킨다

    def form_valid(self, form):
        form.instance.author_id = self.request.user.id  # 현재 열려있는 유저 아이디랑 연결시킨다
        if form.is_valid():  # 입력없을때 액션하면 오류막아줌
            form.instance.save()  # 값이 있으면 save
            return redirect('/')
        else:
            return self.render_to_response({'form': form})  # 값이없으면 여기로보낸다


class PhotoDeleteView(DeleteView):
    model = Photo
    success_url = '/'  # 성공하면 리스트페이지로 넘긴다
    template_name = 'photo/delete.html'  # suffix는 정해진 이름이 있으면 뒤에 알아서 붙여주고... 통일되서 쓸수있고.. 간략하게 적으려고 하는거다.


class PhotoUpdateView(UpdateView):  # 수정
    model = Photo
    fields = ['photo', 'text']  # 수정 필드
    template_name = 'photo/update.html'


def photo_list(request):  # 리스트 페이지를 보여주기 위한... 데이터를 html로 통채로 넘겨주고 html에서 처리하게한다.
    photos = Photo.objects.all()  # 데이터를 전부 photos에 담겠다
    return render(request, 'photo/list.html', {'photos': photos})
    # photoslist req 되면 (photo/list.html 주소일때) {'photos:photos}를 불러온다.
