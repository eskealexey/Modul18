from django.shortcuts import render
from .forms import UserRegister

def check_value(users: list, name: str, pas1: str, pas2: str, age: int) -> bool:
    if (name not in users) and (pas1 == pas2) and age > 18:
        return True

def sign_up_by_html(request):
    title = 'Регистрация html'
    users = ['Alex', 'Tom', 'Nik', 'Roza']
    info= {'title': title,}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = request.POST.get('age')

        if check_value(users, username, password, repeat_password, int(age)):
            info = {'res': f'Приветствуем, {username}!'}
        if username in users:
            info = {'error': 'Пользователь уже существует'}
        elif int(age) < 18:
            info = {'error': 'Вы должны быть старше 18'}
        elif password != repeat_password:
            info = {'error': 'Пароли не совпадают'}

    return render(request, 'fifth_task/registration_page.html', context=info)


def sign_up_by_django(request):
    title = 'Регистрация django'
    users = ['Alex', 'Tom', 'Nik', 'Roza']
    info = {'title': title, }
    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']

            if check_value(users, username, password, repeat_password, int(age)):
                info = {'res': f'Приветствуем, {username}!'}
            if username in users:
                info = {'error': 'Пользователь уже существует'}
            elif int(age) < 18:
                info = {'error': 'Вы должны быть старше 18'}
            elif password != repeat_password:
                info = {'error': 'Пароли не совпадают'}
    else:
        form = UserRegister()
        info = {
            'title': title,
            'form': form,
        }

    return render(request, 'fifth_task/registration_page.html', context=info)