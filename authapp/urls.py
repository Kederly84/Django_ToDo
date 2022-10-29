from django.urls import path
from authapp.apps import AuthappConfig
from authapp import views

app_name = AuthappConfig.name

urlpatterns = [
    path('register/', views.CreateUserView.as_view(), name='register'),
    path('', views.CustomLoginView.as_view(), name='login'),
    path('edit/', views.EditUserView.as_view(), name='edit'),
    path('password/', views.CustomPasswordChangeView.as_view(), name='password'),
    path('logout/', views.CustomLogoutView.as_view(), name='logout'),
]
