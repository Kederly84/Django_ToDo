from django.urls import path
from todo import views
from todo.apps import TodoConfig

app_name = TodoConfig.name

urlpatterns = [
    path('home/', views.example, name='home'),
]
