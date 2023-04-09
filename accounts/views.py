from django.shortcuts import render, redirect, HttpResponse
from .models import UserModel
from django.contrib.auth import login, logout

# Create your views here.

def signup(request):
    if request.method == 'GET':
        return render(request, '/accounts/signup.html')
    elif request.method == 'POST':
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        password2 = request.POST.get('password2', None)
        bio = request.POST.get('bio', None)

        if password != password2:
            return render(request, 'accounts/signup.html')
        else:
            new_user = UserModel()
            new_user.username = username
            new_user.password = password
            new_user.bio = bio
            new_user.save()
        return redirect('/login')
    
def user_login(request):
    if request.method == 'GET':
        return render(request, 'accounts/login.html')

    elif request.method == 'POST':
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)

        me = UserModel.objects.get(username=username)  # 사용자 불러오기
        if me.password == password:  # 저장된 사용자의 패스워드와 입력받은 패스워드 비교
            request.session['user'] = me.username  # 세션에 사용자 이름 저장
            return redirect('/erp')
        else: # 로그인이 실패하면 다시 로그인 페이지를 보여주기
            return redirect('/login')
    # 로그인 view

def user_logout(request):
    pass
    # 로그아웃 view