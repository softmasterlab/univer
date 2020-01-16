from django.shortcuts import render


def reg(request):
    if request.method == 'GET':
        return render(request, 'account/reg.html')
    elif request.method == 'POST':
        # Получаем данные из формы регистрации:
        login = request.POST.get('login')
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')
        email = request.POST.get('email')

        # Проверяем доставку данных:
        data = dict()
        data['message'] = 'ku-ku'
        data['login'] = login
        data['pass1'] = pass1
        data['pass2'] = pass2
        data['email'] = email

        return render(request, 'account/reg_res.html', context=data)


def entry(request):
    return render(request, 'account/entry.html')


def exit(request):
    return render(request, 'account/exit.html')


def reset(request):
    return render(request, 'account/reset.html')
