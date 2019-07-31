from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth

# Create your views here.

def signup(request):
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            try :
                user = User.objects.get(username = request.POST['username'])
                return render(request, 'signup.html', {'error': '이미 사용하고 있는 이름입니다!'})
            except User.DoesNotExist:
                user = User.objects.create_user(
                    request.POST['username'], password = request.POST['password1']
                )
                auth.login(request, user)
                return redirect('/')
    return render(request, 'signup.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']   
        user = auth.authenticate(request, username = username, password = password)
        if user is not None: 
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {'error' : '아이디나 비밀번호를 확인해주세요'})
    else:
        return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return render(request, 'login.html')

