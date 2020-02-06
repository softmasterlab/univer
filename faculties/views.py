from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from .models import Faculty
from .forms import FacultyForm, FacultyForm2


def index(request):
    data = dict()
    all_faculties = Faculty.objects.all()
    data['faculties'] = all_faculties
    paginator = Paginator(all_faculties, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    data['page_obj'] = page_obj
    return render(request, 'faculties/index.html', context=data)


def create(request):
    data = dict()
    if request.method == 'GET':
        faculty_form = FacultyForm()
        data['form'] = faculty_form
        return render(request, 'faculties/create.html', context=data)
    elif request.method == 'POST':
        faculty_form = FacultyForm(request.POST, request.FILES)
        faculty_form.save()
        return redirect('/faculties')


def details(request, fid: int):
    data = dict()
    data['faculty'] = Faculty.objects.get(id=fid)
    return render(request, 'faculties/details.html', context=data)


def edit(request, fid: int):
    data = dict()
    faculty = Faculty.objects.get(id=fid)
    if request.method == 'GET':
        data['form'] = FacultyForm2(instance=faculty)
        data['faculty'] = faculty
        return render(request, 'faculties/edit.html', context=data)
    elif request.method == 'POST':
        faculty_form = FacultyForm2(request.POST)
        if faculty_form.is_valid():
            faculty.title = faculty_form.cleaned_data['title']
            faculty.about = faculty_form.cleaned_data['about']
            faculty.content = faculty_form.cleaned_data['content']
            faculty.site = faculty_form.cleaned_data['site']
            faculty.save()
        return redirect('/faculties')


def delete(request, fid: int):
    data = dict()
    faculty = Faculty.objects.get(id=fid)
    if request.method == 'GET':
        data['faculty'] = faculty
        return render(request, 'faculties/delete.html', context=data)
    elif request.method == 'POST':
        faculty.delete()
        return redirect('/faculties')
