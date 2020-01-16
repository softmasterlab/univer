from django.urls import path
from .views import reg, entry, exit, reset

urlpatterns = [
    path('reg', reg),
    path('entry', entry),
    path('exit', exit),
    path('reset', reset)
]