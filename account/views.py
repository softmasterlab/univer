from django.shortcuts import render
from django.contrib.auth.models import User


def reg(request):
    if request.method == 'GET':
        return render(request, 'account/reg.html')
    elif request.method == 'POST':
        # Получаем данные из формы регистрации:
        login = request.POST.get('login')
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')
        email = request.POST.get('email')

        # Валидация данных будет здесь .....

        # Проверка доставки данных:
        data = dict()
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
            data['report'] = 'Регистрация провалена!'
        else:
            data['color'] = 'green'
            data['report'] = 'Регистрация успешно завершена!'

        # Загрузка страницы отчета по результатам регистрации:
        return render(request, 'account/reg_res.html', context=data)


def entry(request):
    return render(request, 'account/entry.html')


def exit(request):
    return render(request, 'account/exit.html')


def reset(request):
    return render(request, 'account/reset.html')
