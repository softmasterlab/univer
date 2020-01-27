from django.urls import path
from .views import reg, entry, exit, reset, ajax_reg

urlpatterns = [
    path('reg', reg),
    path('entry', entry),
    path('exit', exit),
    path('reset', reset),
    path('ajax_reg', ajax_reg)
]