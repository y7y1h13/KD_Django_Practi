from django.shortcuts import render
from .models import User
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password


def register(request):
    if request.method == 'GET':
        return render(request, 'user/register.html')
    elif request.method == 'POST':
        username = request.POST.get('username', None)
        useremail = request.POST.get('useremail', None)
        password = request.POST.get('password', None)
        re_password = request.POST.get('re-password', None)
        gender = request.POST.get('gender', None)
        job = request.POST.get('job', None)

        res_data = ''
        if not (username and useremail and password and re_password and gender):
            res_data = '값을 입력해 주세요!'
        elif password != re_password:
            res_data = '비밀번호가 다릅니다.'
        else:
            user = User(
                username = username,
                useremail = useremail,
                password = make_password(password),
                gender = gender,
                job = job,
            )
            user.save()
        return render(request, 'user/register.html', {'res_data':res_data})