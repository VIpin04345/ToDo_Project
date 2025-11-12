from django.urls import path
from . import views

urlpatterns = [
    path("", views.task_list, name="task_list"),
    path("toggle/<int:pk>/", views.toggle_completed, name="toggle_completed"),
    path("delete/<int:pk>/", views.task_delete, name="delete"),
]
