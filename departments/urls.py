from django.urls import path, re_path
from .views import create, details, delete, edit

urlpatterns = [
    path('create', create),
    re_path(r'^edit/(?P<dep_id>[0-9]+)$', edit),
    re_path(r'^details/(?P<dep_id>[0-9]+)$', details),
    re_path(r'^delete/(?P<dep_id>[0-9]+)$', delete)
]
