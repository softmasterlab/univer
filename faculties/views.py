from django.shortcuts import render, redirect
from .models import Faculty
from .forms import FacultyForm


def index(request):
    data = dict()
    all_faculties = Faculty.objects.all()
    data['faculties'] = all_faculties
    return render(request, 'faculties/index.html', context=data)


def create(request):
    data = dict()
    if request.method == 'GET':
        faculty_form = FacultyForm()
        data['form'] = faculty_form
        return render(request, 'faculties/create.html', context=data)
    elif request.methd == 'POST':
        faculty_form = FacultyForm(request.POST, request.FILES)
        faculty_form.save()
        return redirect('/faculties')


def details(request, fid: int):
    data = dict()
    data['faculty'] = Faculty.objects.get(id=fid)
    return render(request, 'faculties/details.html', context=data)


def edit(request, fid: int):
    data = dict()
    data['faculty'] = Faculty.objects.get(id=fid)
    return render(request, 'faculties/details.html', context=data)


def delete(request, fid: int):
    data = dict()
    data['faculty'] = Faculty.objects.get(id=fid)
    return render(request, 'faculties/details.html', context=data)
