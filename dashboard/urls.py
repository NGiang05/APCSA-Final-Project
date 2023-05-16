from django.urls import path
from . import views

urlpatterns = [
    path("", views.dashboard),
    path("submit/", views.submit_entry),
    path("teacher/", views.teacher)
]