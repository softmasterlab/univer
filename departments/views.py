from django.shortcuts import render, redirect


def create(request):
    return render(request, 'departments/create.html')


def details(request, dep_id: int):
    return render(request, 'departments/details.html')


def delete(request, dep_id: int):
    return render(request, 'departments/delete.html')


def edit(request, dep_id: int):
    return render(request, 'departments/edit.html')
