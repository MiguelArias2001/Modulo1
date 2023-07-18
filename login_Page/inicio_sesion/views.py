from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from inicio_sesion.Modelo.Usuario import Usuario
from inicio_sesion.Modelo.Usuario_DAO import UsuarioDTO
from inicio_sesion.Modelo.Correo import Correo
import matplotlib.pyplot as plt
import io
import urllib.parse, base64

#Carga de las vistas de los templates
def error_404(request, exception):
    return render(request, '404.html', status=404)

def index(request):
    return render(request,'index.html')

def register(request):
    return render(request,'register.html')

def login(request):
    return render(request,'login.html')

def change_pass(request):
    return render(request,'Recuperacion_contraseña.html')

def request_pass(request):
    return render(request,'Cambio_contraseña.html')

def chat(request):
    return render(request,'chat.html')

def base_usuario(request):
    return render(request,'Base_Usuario.html')

def foro(request):
    return render(request,'Foro.html')

def vista_usuarios(request):
    usuario = Usuario(None,"","","")
    met = UsuarioDTO()
    users = met.view_users(usuario)
    return render(request,'Vista_usuarios.html',{'usuarios': users})

def archivo(request):
    met = UsuarioDTO()
    arch = met.Ver_archivo()
    return render(request,'Archivos.html',{"arch":arch})

def reporte(request):
    met = UsuarioDTO()
    registro = met.Register()
    Data = met.Grafico()

    meses = [d['Mes'] for d in Data]
    visitas = [d['Visitas'] for d in Data]

    fig, ax = plt.subplots()

    # Crea el gráfico de barras usando los datos extraídos
    ax.bar(meses, visitas)

    # Estiliza el gráfico según tus preferencias
    ax.set_xlabel('Mes')
    ax.set_ylabel('Visitas')
    ax.set_title('Visitas por Mes')

    # Guarda el gráfico en un buffer
    buf = io.BytesIO()
    fig.savefig(buf, format='png')
    buf.seek(0)
    string = base64.b64encode(buf.read())
    uri = urllib.parse.quote(string)
    

    return render(request,'Reportes.html',{'registro': registro, 'chart': uri})

def base_administrador(request):
    return render(request,'Base_Administrador.html')

def Config_user(request):
    codigo = request.COOKIES.get('codigo')
    usuario = Usuario(codigo,"","","")
    met = UsuarioDTO()
    user = met.charge_user(usuario)
    context = {'Usuario': user}
    return render(request,'Configuracion.html',context)

def perfil_usuario(request):
    codigo = request.COOKIES.get('codigo')
    admin: int
    admin = request.COOKIES.get('admin')
    usuario = Usuario(codigo,"","","")
    met = UsuarioDTO()
    user = met.charge_user(usuario)
    context = {'Usuario': user, 'admin': admin}
    print(context)
    return render(request,'Perfil.html',context)

#Acciones de las vistas
def usuario(request):   
    codigo = request.COOKIES.get('codigo')
    usuario = Usuario(codigo,"","","")
    met = UsuarioDTO()
    user = met.charge_user(usuario)
    context = {'Usuario':user}#type: ignore
    return render(request,'Base_Usuario.html',context)


@csrf_exempt
def user_session(request):
    if request.method == 'POST':
        correo = request.POST.get('email')
        contra = request.POST.get('password')
        user = Usuario("","",correo,contra)
        met = UsuarioDTO()
        res = met.search_user(user)
        dec: int
        dec = res[0] #type: ignore
        codigo = met.search_code(user)
        if res is not None: #type: ignore
            if dec == 1:
                response = redirect('usuarios')
                response.set_cookie('codigo', codigo[0])#type: ignore
                response.set_cookie('admin', 0)#type: ignore
                del user
                del met
            elif dec == 2: 
                response = redirect('administrador')
                response.set_cookie('codigo', codigo[0])#type: ignore
                response.set_cookie('admin', 1)#type: ignore
                del user
                del met
            else:
                context = {'res': True,'Mensaje':"la contraseña o el usuario no es correcto"}
                response = render(request,"login.html",context)
        else:
            context = {'res': True,'Mensaje':"la contraseña o el usuario no es correcto"}
            response = render(request,"login.html",context)
    return response  # type: ignore

@csrf_exempt
def user_creation(request):
    if request.method == 'POST':
        correo = request.POST.get('Correo')
        contra = request.POST.get('Contrasena')
        nombre = request.POST.get('Nombre')
        codigo = request.POST.get('Codigo')
        user = Usuario(codigo,nombre,correo,contra)
        met = UsuarioDTO()
        met.create_user(user)
        print("Correo: "+correo+" Contraseña: "+contra+" Nombre: "+nombre+" Codigo: "+str(codigo))
    return render(request,'register.html')

@csrf_exempt
def rq_pass(request):
    if request.method == 'POST':
        correo = request.POST.get('email')
        user = Usuario("","",correo,"")
        met = UsuarioDTO()
        if met.User_exist(user):
            mensajero = Correo.get_instance()
            mensajero.recuperacion(correo) # type: ignore
            context = {'res': False}
            print("existe")
            response = render(request,'Recuperacion_contraseña.html',context) 
            response.set_cookie('correo', correo)
        else:
            context = {'res': True,'Mensaje':"El Correo No existe"}
            print("No existe")
            response = render(request,'Recuperacion_contraseña.html',context) 
    return response  # type: ignore

@csrf_exempt
def chg_pass(request):
    if request.method == 'POST':
        contra1 = request.POST.get('Nueva_Contrasena')
        contra2 = request.POST.get('Rep_Contrasena')
        correo = request.COOKIES.get('correo')
        if contra1 == contra2:
            user = Usuario("","",correo,contra1)
            met = UsuarioDTO()
            met.update_pass(user)
            response = render(request,'login.html')
        else:
            context = {'res': True,'Mensaje':"Las Contraseñas no coinciden"}
            response = render(request,'Cambio_contraseña.html',context)
        print("Contraseña: "+contra1+" Contraseña: "+contra2)
    return response  # type: ignore

@csrf_exempt
def validate(request):
    if request.method == 'POST':
        codigo = request.POST.get('Codigo_v')
        mensajero = Correo.get_instance()
        if mensajero.validacion(int(codigo)): # type: ignore
            print(codigo)
            response = render(request,'Cambio_contraseña.html')
            print("existe")
        else:
            print("No existe")
            print(codigo)
            context = {'res': True,'Mensaje':"El codigo no es valido"}
            response = render(request,'Recuperacion_contraseña.html',context)
    return response # type: ignore

@csrf_exempt
def Delete_Acount(request):
    if request.method == 'GET':
        codigo = request.COOKIES.get('codigo')
        user = Usuario(codigo,"","","")
        met = UsuarioDTO()
        print(met.delete_user(user))
         
    context = {'res': True,'Mensaje':"Cuenta eliminada con exito"}
    response = redirect('index')
    response.delete_cookie('codigo')
    return response

@csrf_exempt
def Delete_Acount_Admin(request):
    if request.method == 'GET':
        codigo = request.GET.get('codigo')
        user = Usuario(codigo,"","","")
        met = UsuarioDTO()
        print(met.delete_user(user))
         
    response = redirect('visualizar_u')
    return response

@csrf_exempt
def Update_User(request):
    if request.method == 'POST':
        nombre = request.POST.get('Nom_user')
        correo = request.POST.get('Email_user')
        ant_pass = request.POST.get('Pass_user')
        password = request.POST.get('New_pass')
        pass_con = request.POST.get('Con_pass')
        codigo = request.COOKIES.get('codigo')
        if password == None and pass_con == None:
            user = Usuario(codigo,nombre,correo,ant_pass)
            met = UsuarioDTO()
            met.update_user(user)
            context = {'res': True,'Mensaje':"Cuenta actualizada con exito",'titulo': "Exito"}
            response = redirect('config_u')
        elif password == pass_con:
                user = Usuario(codigo,nombre,correo,password)
                met = UsuarioDTO()
                met.update_user(user)
                print(pass_con)
                context = {'res': True,'Mensaje':"Cuenta actualizada con exito",'titulo': "Exito"}
                response = redirect('config_u')
        else:
            context = {'res': True,'Mensaje':"las contraseñas no Coinciden",'titulo': "Error"}
            response = redirect('config_u')
    return response # type: ignore


@csrf_exempt
def buscar_nombre(request):
    nombre = request.POST.get('bus_nom')
    usuario = Usuario(None,nombre,"","")
    met = UsuarioDTO()
    users = met.search_users_name(usuario)
    return render(request,'Vista_usuarios.html',{'usuarios': users})

@csrf_exempt
def buscar_codigo(request):
    codigo = request.POST.get('bus_cod')
    usuario = Usuario(codigo,"","","")
    met = UsuarioDTO()
    users = met.search_users_code(usuario)
    return render(request,'Vista_usuarios.html',{'usuarios': users})

@csrf_exempt
def buscar_Filter(request):
    op = request.POST.get('opcion')
    ac = request.POST.get('Opciones')
    filtro = 0
    Activo = 0
    if op == "fecha":
        filtro = 1
    elif op == "nombre":
        filtro = 2
    else:
        filtro = 3
    
    if ac == "Activo":
        Activo = 1
    elif ac == "Inactivo":
        Activo = 0
    else:
        Activo = 2
    print("Resultado:"+ ac)    
    met = UsuarioDTO()
    users = met.search_users_filter(Activo,filtro)
    return render(request,'Vista_usuarios.html',{'usuarios': users})

@csrf_exempt
def subir_archivo(request):
    Nombre = request.POST.get("Nombre_a")
    Descripcion = request.POST.get('Descripcion_a','')
    Archivo = request.FILES['archivo']
    codigo = request.COOKIES.get('codigo')

    contenido = Archivo.read()

    try:
        # Intenta decodificar el contenido como UTF-8
        contenido_decodificado = contenido.decode('utf-8')
    except UnicodeDecodeError:
        # Si la decodificación como UTF-8 falla, intenta con Latin-1
        contenido_decodificado = contenido.decode('latin-1')

    met = UsuarioDTO()
    met.Insertar_archivo(Nombre,Descripcion,contenido_decodificado,codigo)
    arch = met.Ver_archivo()
    return render(request,'Archivos.html',{"arch":arch})

@csrf_exempt
def actualizar_archivo(request):
    codigo = request.POST.get("codigo")
    print(codigo)
    met = UsuarioDTO()
    met.Actualizar_Archivo(codigo,1)
    arch = met.Ver_archivo()
    return render(request,'Archivos.html',{"arch":arch})

@csrf_exempt
def Filtrar_archivos(request):
    op = request.POST.get("status")
    met = UsuarioDTO()
    if op == "no-leido":
        arch = met.Filtro_Archivo(0)
    elif op == "leido":
        arch = met.Filtro_Archivo(1)
    elif op == "Todo":
        arch = met.Ver_archivo()
    else:
        arch = met.Ver_archivo()
    return render(request,'Archivos.html',{"arch":arch})

@csrf_exempt
def Eliminar_archivo(request):
    codigo = request.POST.get("codigo")
    print(codigo)
    met = UsuarioDTO()
    met.Eliminar_archivo(codigo)
    arch = met.Ver_archivo()
    return render(request,'Archivos.html',{"arch":arch})