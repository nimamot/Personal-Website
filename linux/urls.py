from django.contrib import admin
from . import views
from django.urls import path


app_name = 'linux'
urlpatterns = [
    path('', views.all_linux, name='all_linux'),
    path('<int:linux_id>/', views.detail, name='detail')
]
