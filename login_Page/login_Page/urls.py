from django.contrib import admin
from django.urls import path
from inicio_sesion import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('change_pass/', views.change_pass, name='change_pass'),
    path('request_pass/', views.request_pass, name='request_pass'),
    path('usuario/', views.usuario, name='usuarios'),
    path('user_session/', views.user_session, name='user_session'),
    path('user_creation/', views.user_creation, name='user_creation'),
    path('rq_pass/', views.rq_pass, name='rq_pass'),
    path('chg_pass/', views.chg_pass, name='chg_pass'),
    path('validate/', views.validate, name='validate'),
]

handler404 = 'inicio_sesion.views.error_404'