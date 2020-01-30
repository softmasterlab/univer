from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import JsonResponse


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
        login = request.POST.get('login')
        pass1 = request.POST.get('pass1')

        # Проверка доставки данных:
        data['message'] = 'ku-ku'
        data['login'] = login
        data['pass1'] = pass1

        # Загрузка страницы отчета по результатам авторизации:
        return render(request, 'account/entry_res.html', context=data)


def exit(request):
    return render(request, 'account/exit.html')


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
