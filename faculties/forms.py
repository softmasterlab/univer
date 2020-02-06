from django import forms
from .models import Faculty


class FacultyForm(forms.ModelForm):
    class Meta:
        model = Faculty
        fields = ('title', 'about', 'content', 'picture', 'photo', 'site')


class FacultyForm2(forms.ModelForm):
    class Meta:
        model = Faculty
        fields = ('title', 'about', 'content', 'site')
