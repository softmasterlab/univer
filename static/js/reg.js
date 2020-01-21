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

    $('#login').blur(function () {
        let _login = $(this).val();
        if (regExp1.test(_login)) {
            $('#login_ico').attr('src', '../../static/img/ok.png');
            $('#login_err').text('');
        } else {
            $('#login_ico').attr('src', '../../static/img/cross.png');
            $('#login_err').text('Логин должен быть буквенно-цифорвым, длиной от 6 до 16 символов');
        }


    });

    $('#login').focus(function () {
        $('#login_ico').attr('src', '');
        $('#login_err').text('');
    });

});
