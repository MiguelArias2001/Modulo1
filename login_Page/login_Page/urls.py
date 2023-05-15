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
    path('chat/', views.chat, name='chat'),
    path('perfil_u/', views.perfil_usuario, name='perfil_u'),
    path('config_u/', views.Config_user, name='config_u'),
    path('foro/', views.foro, name='foro'),
    path('base_user/', views.base_usuario, name='base_user'),
    path('eliminar_u/',views.Delete_Acount, name='eliminar_u'),
    path('actualizar_u/',views.Update_User, name='actualizar_u'),
]

handler404 = 'inicio_sesion.views.error_404' 