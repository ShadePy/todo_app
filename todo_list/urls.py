from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.index, name="home"),
    path("delete_all", views.delete_all, name="delete_all"),
    path("delete_complete", views.delete_complete, name="delete_complete"),
    path("add", views.add_todo, name="add"),
    path("todo_change/<todo_id>", views.todo_change, name="todo_change"),
]

