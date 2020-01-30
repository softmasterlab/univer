from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.contrib.auth import authenticate, login, logout


def reg(request):
    if request.method == 'GET':
        return render(request, 'account/reg.html')
    elif request.method == 'POST':
        # Создаем словарь отчета:
        data = dict()

        # Получаем данные из формы регистрации:
        login = request.POST.get('login')
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')
        email = request.POST.get('email')

        # Проверка совпадения паролей:
        if pass1 != pass2:
            data['color'] = 'red'
            data['report'] = 'Пароли не совпадают!'
        else:
            # Проверка доставки данных:
            """
            data['message'] = 'ku-ku'
            data['login'] = login
            data['pass1'] = pass1
            data['pass2'] = pass2
            data['email'] = email
            """

            # Добавление пользователя в базу:
            user = User.objects.create_user(login, email, pass1)
            user.save()

            # Формирование отчета о результатах попытки регистрации:
            if user is None:
                data['color'] = 'red'
                data['report'] = 'В регистрации отказано!'
            else:
                data['color'] = 'green'
                data['report'] = 'Регистрация успешно завершена!'

        # Загрузка страницы отчета по результатам регистрации:
        return render(request, 'account/reg_res.html', context=data)


def entry(request):
    if request.method == 'GET':
        return render(request, 'account/entry.html')
    elif request.method == 'POST':
        # Создаем словарь для передачи сообщений на страницу отчета
        data = dict()
        data['color'] = 'purple'
        data['report'] = 'Test Report'

        # Получаем данные из формы авторизации:
        _login = request.POST.get('login')
        _pass1 = request.POST.get('pass1')

        # Проверка доставки данных:
        data['login'] = _login
        data['pass1'] = _pass1

        # Аутентификация пользователя:
        user = authenticate(request, username=_login, password=_pass1)
        if user is not None:
            data['color'] = 'green'
            data['report'] = 'Вы успешно авторизованы!'
            login(request, user)
            return redirect('/home')
        else:
            data['color'] = 'red'
            data['report'] = 'Пользователь не найден!'
            # Загрузка страницы отчета по результатам авторизации:
            return render(request, 'account/entry_res.html', context=data)


def exit(request):
    logout(request)
    return redirect('/home')


def reset(request):
    return render(request, 'account/reset.html')


def ajax_reg(request):
    response = dict()
    _login = request.GET.get('login')

    try:
        User.objects.get(username=_login)
        response['mess'] = 'занят'
    except User.DoesNotExist:
        response['mess'] = 'свободен'

    return JsonResponse(response)


def profile(request):
    return render(request, 'account/profile.html')