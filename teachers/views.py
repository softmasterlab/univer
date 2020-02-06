from django.shortcuts import render, redirect


def create(request):
    return render(request, 'teachers/create.html')


def details(request, teach_id: int):
    return render(request, 'teachers/details.html')


def delete(request, teach_id: int):
    return render(request, 'teachers/delete.html')


def edit(request, teach_id: int):
    return render(request, 'teachers/edit.html')
