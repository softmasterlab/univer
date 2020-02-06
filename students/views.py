from django.shortcuts import render, redirect


def create(request):
    return render(request, 'students/create.html')


def details(request, stud_id: int):
    return render(request, 'students/details.html')


def delete(request, stud_id: int):
    return render(request, 'students/delete.html')


def edit(request, stud_id: int):
    return render(request, 'students/edit.html')
