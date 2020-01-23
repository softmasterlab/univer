function example() {
    // Демонстарционный пример:
    //-------------------------------------------
    alert('Привет, JavaScript!');
    let name = prompt('Как Вас зовут?');
    alert('Будем знакомы, ' + name);
    let result = confirm('Перейти на Bing.com?');
    if (result == true) {
        window.location = 'http://bing.com';
    } else {
        alert('Ну не хотите, - и не надо!');
    }
    //-------------------------------------------
}

$(document).ready(function () {

    let valid = false;
    let regExp1 = /^[a-zA-Z][a-zA-Z0-9_\-]{5,15}$/;
    let regExp2 = /^(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9])[A-Za-z0-9_\-]{8,}$/;

    // Проверки корректности введенных данных:
    // ---------------------------------------
    // 1 -> Валидация логина:
    $('#login').blur(function () {
        let _login = $(this).val();
        if (regExp1.test(_login)) {
            $('#login_ico').attr('src', '../../static/img/ok.png');
            $('#login_err').text('');
            // Проверка занятости логина:
            //$.ajax({

            //});
            valid = true;
        } else {
            $('#login_ico').attr('src', '../../static/img/cross.png');
            $('#login_err').text('Логин должен быть буквенно-цифорвым, длиной от 6 до 16 символов');
            valid = false;
        }


    });

    // 2 -> Валидация пароля:
    $('#pass1').blur(function () {
        let _pass1 = $(this).val();
        if (regExp2.test(_pass1)) {
            $('#pass1_ico').attr('src', '../../static/img/ok.png');
            $('#pass1_err').text('');
            valid = true;
        } else {
            $('#pass1_ico').attr('src', '../../static/img/cross.png');
            $('#pass1_err').text('Пароль должен быть строгим буквенно-цифорвым, длиной от 8 символов');
            valid = false;
        }
    });

    // 3 -> Валидация подтверждения:
    $('#pass2').blur(function () {
        let _pass2 = $(this).val();
        if (regExp2.test(_pass2)) {
            $('#pass2_ico').attr('src', '../../static/img/ok.png');
            $('#pass2_err').text('');
            valid = true;
        } else {
            $('#pass2_ico').attr('src', '../../static/img/cross.png');
            $('#pass2_err').text('Пароль должен быть строгим буквенно-цифорвым, длиной от 8 символов');
            valid = false;
        }
    });

    // 4 -> Валидация E-Mail:
    $('#email').blur(function () {
        let _email = $(this).val();
        if (regExp1.test(_email)) {
            $('#email_ico').attr('src', '../../static/img/ok.png');
            $('#email_err').text('');
            valid = true;
        } else {
            $('#email_ico').attr('src', '../../static/img/cross.png');
            $('#email_err').text('E-Mail должен быть буквенно-цифорвым, длиной от 6 до 16 символов');
            valid = false;
        }
    });

    // Сброс сообщений об ошибках:
    // ---------------------------
    $('#login').focus(function () {
        $('#login_ico').attr('src', '');
        $('#login_err').text('');
    });

    $('#pass1').focus(function () {
        $('#pass1_ico').attr('src', '');
        $('#pass1_err').text('');
    });

    $('#pass2').focus(function () {
        $('#pass2_ico').attr('src', '');
        $('#pass2_err').text('');
    });

    $('#email').focus(function () {
        $('#email_ico').attr('src', '');
        $('#email_err').text('');
    });

    // Определение статуса валидности всех полей:
    // ------------------------------------------
    $('#submit').click(function () {
        if (valid == true) {
            $('#form1').attr('onsubmit', 'return true');
        } else {
            $('#form1').attr('onsubmit', 'return false');
            alert('Форма содержит некорректные данные! \nОтправка данных заблокирована!');
        }
    });

});
