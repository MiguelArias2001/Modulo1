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
    path('vista_usuario/',views.vista_usuarios, name='visualizar_u'),
    path('archivo/',views.archivo, name='archivo'),
    path('reporte/',views.reporte, name='reporte'),
    path('administrador/',views.base_administrador, name='administrador'),
    path('Delete_user/',views.Delete_Acount_Admin, name='delete_user'),
    path('Search_name/',views.buscar_nombre, name='busca_nombre'),
    path('Search_code/',views.buscar_codigo, name='busca_code'),
    path('Filter_user/',views.buscar_Filter, name='busca_filter'),
    path('cargar_archivo/',views.subir_archivo, name='carga_archivo'),
    path('actualizar_archivo/',views.actualizar_archivo, name='actualiza_archivo'),
    path('Filtro_archivo/',views.Filtrar_archivos, name='filtro_archivo'),
    path('Eliminar_archivo/',views.Eliminar_archivo, name='eliminar_archivo'),
]

handler404 = 'inicio_sesion.views.error_404' 