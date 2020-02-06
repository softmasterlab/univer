from django.shortcuts import render, redirect


def create(request):
    return render(request, 'employees/create.html')


def details(request, emp_id: int):
    return render(request, 'employees/details.html')


def delete(request, emo_id: int):
    return render(request, 'employees/delete.html')


def edit(request, emp_id: int):
    return render(request, 'employees/edit.html')
