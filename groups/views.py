from django.shortcuts import render, redirect


def create(request):
    return render(request, 'groups/create.html')


def details(request, group_id: int):
    return render(request, 'groups/details.html')


def delete(request, group_id: int):
    return render(request, 'groups/delete.html')


def edit(request, group_id: int):
    return render(request, 'groups/edit.html')
