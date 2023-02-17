from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import UserCreationForm, VerifyForm
from . import verify
from .decorators import verification_required


#Этот декоратор позволит пользователям, вошедшим в систему, получить доступ к представлению, 
#но перенаправит пользователей, которые не вошли в систему, на страницу входа. URL в config/settings.py = LOGIN_URL = '/login/'
@login_required 
@verification_required #проверяет is_verified
def index(request):
    return render(request, 'index.html')


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            verify.send(form.cleaned_data.get('phone')) #отправляет код на номер телефона сразу после сохранения пользователя в бд
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})




@login_required
#проверка на верификацию пользователя
def verify_code(request):
    if request.method == 'POST':
        form = VerifyForm(request.POST)
        if form.is_valid():
            code = form.cleaned_data.get('code')
            if verify.check(request.user.phone, code):
                request.user.is_verified = True
                request.user.save()
                return redirect('index')
    else:
        form = VerifyForm()
    return render(request, 'verify.html', {'form': form})